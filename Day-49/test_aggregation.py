import pandas as pd


def aggregate(df):

    return df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()


def test_aggregation():

    data = [
        {"endpoint": "/login", "response_time": 100, "status_code": 200},
        {"endpoint": "/login", "response_time": 200, "status_code": 500},
        {"endpoint": "/orders", "response_time": 300, "status_code": 200}
    ]

    df = pd.DataFrame(data)

    result = aggregate(df)

    login_row = result[result["endpoint"] == "/login"].iloc[0]

    assert login_row["total_requests"] == 2
    assert login_row["avg_latency"] == 150
    assert login_row["error_rate"] == 0.5

    print("test_aggregation passed")


if __name__ == "__main__":
    test_aggregation()