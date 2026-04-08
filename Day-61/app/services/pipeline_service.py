import pandas as pd
from app.services.enrichment_service import enrich_data_with_external

REQUIRED_COLUMNS = {"timestamp", "endpoint", "response_time", "status_code"}

def validate(df):
    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise ValueError("Invalid CSV structure")

def clean(df):
    df = df[df["response_time"] >= 0]
    df = df.dropna(subset=["endpoint"])
    return df

def transform(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    return df

def aggregate(df):
    return {
        "total_requests": len(df),
        "avg_latency": round(df["response_time"].mean(), 2),
        "error_rate": round((df["status_code"] >= 400).mean(), 2),
        "request_per_source": df["external_info"].value_counts().to_dict()
    }

async def process_pipeline(file_path: str):

    df = pd.read_csv(file_path)

    total_records = len(df)
    
    validate(df)
    
    df = clean(df)
    valid_records = len(df)

    df = transform(df)
    
    # convert DataFrame --> list of Dicts
    records = df.to_dict(orient="records")

    # Enrich
    enrich_records = await enrich_data_with_external(records)

    # Convert back to DataFrame
    df = pd.DataFrame(enrich_records)
    
    metrics = aggregate(df)
    
    return {
        "total_records": total_records,
        "valid_records": valid_records,
        **metrics
    }