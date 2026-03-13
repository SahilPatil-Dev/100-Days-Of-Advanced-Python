import pandas as pd
import json


def export_to_json(df: pd.DataFrame, output_file: str):

    # Convert DataFrame → list of dicts
    records = df.to_dict(orient="records")

    with open(output_file, "w") as f:
        json.dump(records, f, indent=2, default=str)

    print(f"JSON report saved → {output_file}")


if __name__ == "__main__":

    data = {
        "endpoint": ["/login", "/orders", "/profile"],
        "total_requests": [120, 80, 40],
        "avg_latency": [120.5, 340.2, 90.1],
        "error_rate": [0.02, 0.05, 0.01]
    }

    df = pd.DataFrame(data)

    export_to_json(df, "analytics_report.json")