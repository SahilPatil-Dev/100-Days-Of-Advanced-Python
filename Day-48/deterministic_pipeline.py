import pandas as pd
import numpy as np


def generate_dataset(seed=42):

    np.random.seed(seed)

    data = {
        "endpoint": np.random.choice(
            ["/login", "/orders", "/profile"], 1000
        ),
        "response_time": np.random.normal(200, 50, 1000),
        "status_code": np.random.choice([200, 200, 404, 500], 1000)
    }

    df = pd.DataFrame(data)

    return df


def deterministic_pipeline():

    df = generate_dataset()

    # Always sort for deterministic output
    df = df.sort_values(by=["endpoint"]).reset_index(drop=True)

    report = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    return report


if __name__ == "__main__":

    result = deterministic_pipeline()

    print(result)