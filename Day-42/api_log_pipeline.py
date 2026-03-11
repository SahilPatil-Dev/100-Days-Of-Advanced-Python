import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
def run_api_log_pipeline(input_file: str, output_file: str):

    print("Loading logs...")
    df = pd.read_csv(input_file)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    print("Cleaning logs...")
    df = df.dropna(subset=["endpoint"])
    df = df[df["response_time"] >= 0]

    df["response_time"] = df["response_time"].fillna(
        df["response_time"].mean()
    )

    print("Transforming dataset...")
    df["hour"] = df["timestamp"].dt.hour

    print("Aggregating metrics...")

    report = df.groupby("endpoint").agg(
        requests_per_endpoint=("endpoint", "count"),
        average_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    print("Saving analytics report...")
    report.to_csv(output_file, index=False)

    print("Pipeline finished.")
    print(report)


if __name__ == "__main__":
    run_api_log_pipeline(
        "api_logs.csv",
        "api_analytics_report.csv"
    )