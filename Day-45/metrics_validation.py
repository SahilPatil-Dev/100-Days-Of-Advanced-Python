import pandas as pd


class MetricsValidationError(Exception):
    pass


def validate_metrics(report_df: pd.DataFrame):

    errors = []

    if (report_df["avg_latency"] < 0).any():
        errors.append("Average latency cannot be negative")

    if (report_df["error_rate"] > 1).any():
        errors.append("Error rate cannot exceed 1")

    if (report_df["total_requests"] <= 0).any():
        errors.append("Total requests must be greater than 0")

    if errors:
        raise MetricsValidationError("; ".join(errors))

    return True