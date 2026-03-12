import pandas as pd
from schema_validator import validate_record, ValidationError


def run_pipeline(filepath: str):

    df = pd.read_csv(filepath)

    valid_records = []
    invalid_records = []

    # Validation stage
    for _, row in df.iterrows():

        record = row.to_dict()

        try:
            validated = validate_record(record)
            valid_records.append(validated)

        except ValidationError:
            invalid_records.append(record)

    valid_df = pd.DataFrame(valid_records)

    # Transform stage
    valid_df["hour"] = valid_df["timestamp"].dt.hour

    # Aggregation stage
    report = valid_df.groupby("endpoint").agg(
        total_requests=("endpoint", "count"),
        average_latency=("response_time", "mean"),
        error_rate=("status_code", lambda x: (x >= 400).mean())
    ).reset_index()

    print("Pipeline Report")
    print(report)

    print("\nValidation Stats")
    print("Valid records:", len(valid_records))
    print("Invalid records:", len(invalid_records))

    return report


if __name__ == "__main__":
    run_pipeline("api_logss.csv")