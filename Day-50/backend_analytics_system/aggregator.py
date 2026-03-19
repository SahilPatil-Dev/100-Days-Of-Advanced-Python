import pandas as pd

def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    
    report = df.groupby("endpoint").agg(
        total_requests = ("endpoint", "count"),
        avg_latency = ("response_time", "mean"),
        error_rate = ("status_code", lambda x: (x >= 400).mean())
    ).reset_index()
    
    return report