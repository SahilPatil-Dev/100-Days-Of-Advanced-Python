import pandas as pd
import numpy as np
import time


def generate_dataset(size=1_000_000):
    """Simulate large log dataset"""
    data = {
        "endpoint": np.random.choice(
            ["/login", "/orders", "/profile", "/checkout"], size
        ),
        "response_time": np.random.normal(200, 50, size),
        "status_code": np.random.choice([200, 200, 200, 404, 500], size),
        "extra_column": np.random.random(size)
    }
    return pd.DataFrame(data)


def inefficient_pipeline(df):
    """Pipeline with redundant computation"""

    start = time.perf_counter()

    # recompute multiple times
    total_requests = df.groupby("endpoint").size()
    avg_latency = df.groupby("endpoint")["response_time"].mean()
    error_rate = df.groupby("endpoint")["status_code"].apply(lambda x: (x >= 400).mean())

    result = pd.concat(
        [total_requests, avg_latency, error_rate],
        axis=1
    )

    end = time.perf_counter()

    print("Inefficient pipeline runtime:", end - start)
    return result


def optimized_pipeline(df):
    """Optimized pipeline"""

    start = time.perf_counter()

    # only required columns
    df = df[["endpoint", "response_time", "status_code"]]

    result = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    )

    end = time.perf_counter()

    print("Optimized pipeline runtime:", end - start)
    return result


if __name__ == "__main__":

    df = generate_dataset()

    inefficient_pipeline(df)
    optimized_pipeline(df)