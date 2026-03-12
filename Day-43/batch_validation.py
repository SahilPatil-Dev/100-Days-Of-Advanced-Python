import pandas as pd
from schema_validator import validate_record, ValidationError


def validate_dataset(filepath: str):

    df = pd.read_csv(filepath)

    valid_records = []
    invalid_records = []

    for _, row in df.iterrows():

        record = row.to_dict()

        try:
            validated = validate_record(record)
            valid_records.append(validated)

        except ValidationError as e:
            record["error"] = str(e)
            invalid_records.append(record)

    print("Validation Summary")
    print("-------------------")
    print("Valid records:", len(valid_records))
    print("Invalid records:", len(invalid_records))

    return valid_records, invalid_records


if __name__ == "__main__":
    validate_dataset("api_logss.csv")