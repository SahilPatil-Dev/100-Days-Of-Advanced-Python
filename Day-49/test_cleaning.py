import pandas as pd


def clean_data(df):
    df = df[df["response_time"] >= 0]
    df = df[df["endpoint"].notna()]
    df = df[df["endpoint"] != ""]
    return df


def test_cleaning():

    data = [
        {"endpoint": "/login", "response_time": 100},
        {"endpoint": "/orders", "response_time": -10},   # invalid
        {"endpoint": None, "response_time": 200},        # invalid
        {"endpoint": "", "response_time": 150}           # invalid
    ]

    df = pd.DataFrame(data)

    cleaned = clean_data(df)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["endpoint"] == "/login"

    print("test_cleaning passed")


if __name__ == "__main__":
    test_cleaning()