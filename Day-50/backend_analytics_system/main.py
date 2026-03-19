from loader import load_data
from validator import validate_data
from cleaner import clean_data
from transformer import transform_data
from aggregator import aggregate_data
from exporter import export_reports
from monitor import run_monitoring
from logger import log


def run_pipeline():

    log("Pipeline started")

    df = load_data("api_logs.csv")

    df = validate_data(df)
    df = clean_data(df)
    df = transform_data(df)

    report = aggregate_data(df)

    export_reports(report)

    run_monitoring(df, report)

    log("Pipeline completed")


if __name__ == "__main__":
    run_pipeline()