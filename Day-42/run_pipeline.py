from pipeline_stages import (
    load_data,
    clean_data,
    transform_data,
    aggregate_data,
    save_report
)


def run_pipeline(input_file: str, output_file: str):

    print("Step 1: Loading data...")
    df = load_data(input_file)

    print("Step 2: Cleaning data...")
    df = clean_data(df)

    print("Step 3: Transforming data...")
    df = transform_data(df)

    print("Step 4: Aggregating metrics...")
    report = aggregate_data(df)

    print("Step 5: Saving report...")
    save_report(report, output_file)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline("api_logs.csv", "analytics_report.csv")