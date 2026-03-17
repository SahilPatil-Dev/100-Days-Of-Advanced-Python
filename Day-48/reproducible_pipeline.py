import pandas as pd
import numpy as np
from datetime import datetime


LOG_FILE = "execution_log.txt"


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def load_data(seed=42):

    log("Loading dataset")

    np.random.seed(seed)

    data = {
        "endpoint": np.random.choice(
            ["/login", "/orders", "/profile"], 1000
        ),
        "response_time": np.random.normal(200, 50, 1000),
        "status_code": np.random.choice([200, 200, 404, 500], 1000)
    }

    return pd.DataFrame(data)


def clean_data(df):

    log("Cleaning data")

    df = df[df["response_time"] >= 0]

    return df


def transform_data(df):

    log("Transforming data")

    df = df.sort_values(by=["endpoint"]).reset_index(drop=True)

    return df


def aggregate_data(df):

    log("Aggregating data")

    report = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    return report


def save_report(df):

    log("Saving report")

    df.to_csv("final_report.csv", index=False)


def run_pipeline():

    log("Pipeline started")

    df = load_data()
    df = clean_data(df)
    df = transform_data(df)
    report = aggregate_data(df)

    save_report(report)

    log("Pipeline completed")

    return report


if __name__ == "__main__":
    run_pipeline()