import pandas as pd

def load_logs(filepath: str) -> pd.DataFrame:

    df = pd.read_csv(filepath)

    # Parse timestamp column
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    print("Dataset preview:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())

    return df


if __name__ == "__main__":
    df = load_logs("logs.csv")