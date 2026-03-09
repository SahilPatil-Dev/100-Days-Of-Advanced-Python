import pandas as pd


def clean_logs(df: pd.DataFrame) -> pd.DataFrame:

    # Remove rows with missing endpoint
    df = df.dropna(subset=["endpoint"])

    # Replace missing response_time with mean
    mean_latency = df["response_time"].mean()
    df["response_time"] = df["response_time"].fillna(mean_latency)

    # Remove invalid response_time values
    df = df[df["response_time"] >= 0]

    return df


if __name__ == "__main__":
    import log_loader

    df = log_loader.load_logs("logs.csv")
    clean_df = clean_logs(df)

    print("\nClean dataset:")
    print(clean_df)