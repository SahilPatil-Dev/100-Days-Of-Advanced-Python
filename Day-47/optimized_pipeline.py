import pandas as pd
import numpy as np
import time


def generate_dataset(size=1_000_000):

    data = {
        "timestamp": pd.date_range("2024-01-01", periods=size, freq="s"),
        "endpoint": np.random.choice(
            ["/login", "/orders", "/profile", "/checkout"], size
        ),
        "response_time": np.random.normal(200, 50, size),
        "status_code": np.random.choice([200, 200, 200, 404, 500], size),
        "irrelevant_column": np.random.random(size)
    }

    return pd.DataFrame(data)


def optimized_pipeline(df):

    start = time.perf_counter()

    df = df[["endpoint", "response_time", "status_code"]].copy()

    df["response_time"] = df["response_time"].astype("float32")
    df["status_code"] = df["status_code"].astype("int16")
    df["endpoint"] = df["endpoint"].astype("category")
    

    df["is_error"] = df["status_code"] >= 400

    result = df.groupby("endpoint", observed=True).agg(
        avg_latency=("response_time", "mean"),
        total_req=("endpoint", "count"),
        error_rate=("is_error", "mean")
    )

    print("Pipeline runtime", time.perf_counter() - start)

    return result


if __name__ == "__main__":

    df = generate_dataset()

    report = optimized_pipeline(df)

    print(report)