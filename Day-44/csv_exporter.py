import pandas as pd


def export_to_csv(df: pd.DataFrame, output_file: str):

    # Ensure column order is correct
    columns = [
        "endpoint",
        "total_requests",
        "avg_latency",
        "error_rate"
    ]

    df = df[columns]

    df.to_csv(output_file, index=False)

    print(f"CSV report saved → {output_file}")


if __name__ == "__main__":

    data = {
        "endpoint": ["/login", "/orders", "/profile"],
        "total_requests": [120, 80, 40],
        "avg_latency": [120.5, 340.2, 90.1],
        "error_rate": [0.02, 0.05, 0.01]
    }

    df = pd.DataFrame(data)

    export_to_csv(df, "analytics_report.csv")