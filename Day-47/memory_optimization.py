import pandas as pd
import numpy as np


def generate_dataset(size=1_000_000):

    data = {
        "user_id": np.random.randint(1, 100000, size),
        "response_time": np.random.normal(200, 50, size),
        "status_code": np.random.choice([200, 404, 500], size)
    }

    return pd.DataFrame(data)


def memory_usage_mb(df):
    return df.memory_usage(deep=True).sum() / 1024**2


def optimize_memory(df):

    print("Memory before optimization:", memory_usage_mb(df), "MB")

    df["user_id"] = df["user_id"].astype("int32")
    df["status_code"] = df["status_code"].astype("int16")
    df["response_time"] = df["response_time"].astype("float32")

    print("Memory after optimization:", memory_usage_mb(df), "MB")

    return df


if __name__ == "__main__":

    df = generate_dataset()

    optimize_memory(df)