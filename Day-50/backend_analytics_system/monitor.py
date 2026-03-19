def run_monitoring(df, report):

    invalid_records = len(df[df["response_time"] < 0])

    high_error = bool((report["error_rate"] > 0.5).any())

    status = "FAIL" if high_error else "PASS"

    print({
        "invalid_records": invalid_records,
        "high_error_detected": high_error,
        "pipeline_status": status
    })