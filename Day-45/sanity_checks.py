import pandas as pd


def run_sanity_checks(df: pd.DataFrame):

    warnings = []

    # Negative response time
    invalid_latency = df[df["response_time"] < 0]
    if not invalid_latency.empty:
        warnings.append(f"Negative response times found: {len(invalid_latency)}")

    # Invalid status codes
    invalid_status = df[~df["status_code"].between(100, 599)]
    if not invalid_status.empty:
        warnings.append(f"Invalid status codes: {len(invalid_status)}")

    # Missing endpoints
    missing_endpoint = df[df["endpoint"].isna() | (df["endpoint"] == "")]
    if not missing_endpoint.empty:
        warnings.append(f"Missing endpoints: {len(missing_endpoint)}")

    return warnings