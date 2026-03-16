import pandas as pd

from sanity_checks import run_sanity_checks
from metrics_validation import validate_metrics, MetricsValidationError


def monitor_pipeline(input_file: str):

    df = pd.read_csv(input_file)

    summary = {
        "total_records_checked": len(df),
        "total_warnings": 0,
        "total_errors": 0,
        "pipeline_status": "PASS"
    }

    # Run sanity checks
    warnings = run_sanity_checks(df)

    summary["total_warnings"] = len(warnings)

    for w in warnings:
        print("WARNING:", w)

    # Generate analytics report
    report = df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        avg_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    # Validate aggregated metrics
    try:
        validate_metrics(report)

    except MetricsValidationError as e:
        print("ERROR:", str(e))
        summary["total_errors"] += 1
        summary["pipeline_status"] = "FAIL"

    print("\nPipeline Monitoring Summary")
    print(summary)

    return summary


if __name__ == "__main__":
    monitor_pipeline("api_logs.csv")