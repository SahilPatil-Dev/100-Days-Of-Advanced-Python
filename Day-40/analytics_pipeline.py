import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def load_logs(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def clean_logs(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["endpoint"])

    mean_latency = df["response_time"].mean()
    df["response_time"] = df["response_time"].fillna(mean_latency)

    df = df[df["response_time"] >= 0]

    return df


def transform_logs(df: pd.DataFrame) -> pd.DataFrame:
    df["hour"] = df["timestamp"].dt.hour
    return df


def aggregate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    metrics = df.groupby("endpoint").agg(
        requests_per_endpoint=("endpoint", "count"),
        average_latency_per_endpoint=("response_time", "mean"),
        error_rate_per_endpoint=("status_code", lambda x: (x >= 400).mean())
    )

    return metrics.reset_index()


def run_pipeline(filepath: str) -> pd.DataFrame:
    df = load_logs(filepath)
    df = clean_logs(df)
    df = transform_logs(df)
    report = aggregate_metrics(df)

    return report


if __name__ == "__main__":
    report = run_pipeline("logs1.csv")
    print("\nFinal Analytics Report:")
    print(report)