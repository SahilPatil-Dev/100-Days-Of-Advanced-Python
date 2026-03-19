import pandas as pd
from ..aggregator import aggregate_data

def test_pipeline():

    data = [
        {"endpoint": "/login", "response_time": 100, "status_code": 200},
        {"endpoint": "/login", "response_time": 200, "status_code": 500}
    ]

    df = pd.DataFrame(data)

    report = aggregate_data(df)

    assert report.iloc[0]["total_requests"] == 2
    assert report.iloc[0]["error_rate"] == 0.5

    print("Pipeline test passed")

if __name__ == "__main__":
    test_pipeline()