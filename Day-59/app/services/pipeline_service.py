import pandas as pd


REQUIRED_COLUMNS = {"timestamp", "endpoint", "response_time", "status_code"}


def process_pipeline(file_path: str):

    df = pd.read_csv(file_path)

    total_records = len(df)

    # Validate columns
    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise ValueError("Invalid CSV structure")

    # Clean
    df = df[df["response_time"] >= 0]
    df = df.dropna(subset=["endpoint"])

    valid_records = len(df)

    # Transform
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour

    # Aggregate
    total_requests = len(df)
    avg_latency = df["response_time"].mean()
    error_rate = (df["status_code"] >= 400).mean()

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "total_requests": total_requests,
        "avg_latency": round(avg_latency, 2),
        "error_rate": round(error_rate, 2)
    }