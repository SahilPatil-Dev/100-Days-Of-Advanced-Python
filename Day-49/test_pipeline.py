import pandas as pd
import os


def run_pipeline(df):

    # Cleaning
    df = df[df["response_time"] >= 0]
    df = df[df["endpoint"].notna()]

    # Aggregation
    report = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    # Save output
    output_file = "test_output.csv"
    report.to_csv(output_file, index=False)

    return report, output_file


def test_pipeline():

    data = [
        {"endpoint": "/login", "response_time": 100, "status_code": 200},
        {"endpoint": "/login", "response_time": -50, "status_code": 500},  # removed
        {"endpoint": "/orders", "response_time": 300, "status_code": 200}
    ]

    df = pd.DataFrame(data)

    report, file_path = run_pipeline(df)

    # Check file exists
    assert os.path.exists(file_path)

    # Check no invalid records
    assert (report["avg_latency"] >= 0).all()

    # Check expected results
    assert "endpoint" in report.columns

    print("test_pipeline passed")


if __name__ == "__main__":
    test_pipeline()