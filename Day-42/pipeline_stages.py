import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load dataset from CSV."""
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean invalid or missing data."""
    df = df.dropna(subset=["endpoint"])

    # Replace missing response_time with mean
    mean_latency = df["response_time"].mean()
    df["response_time"] = df["response_time"].fillna(mean_latency)

    # Remove invalid response times
    df = df[df["response_time"] >= 0]

    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Extract time-based features."""
    df["hour"] = df["timestamp"].dt.hour
    return df


def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Generate analytics metrics."""
    report = df.groupby("endpoint").agg(
        requests_per_endpoint=("endpoint", "count"),
        average_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    return report


def save_report(df: pd.DataFrame, output_path: str):
    """Save final report."""
    df.to_csv(output_path, index=False)