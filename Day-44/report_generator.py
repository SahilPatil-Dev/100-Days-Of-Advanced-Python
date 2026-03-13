import pandas as pd
import json


def generate_report(input_file: str):

    df = pd.read_csv(input_file)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    report = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    # Export CSV
    report.to_csv("analytics_report.csv", index=False)

    # Export JSON
    records = report.to_dict(orient="records")

    with open("analytics_report.json", "w") as f:
        json.dump(records, f, indent=2, default=str)

    print("Reports generated:")
    print("analytics_report.csv")
    print("analytics_report.json")

    return report


if __name__ == "__main__":
    generate_report("api_logs.csv")