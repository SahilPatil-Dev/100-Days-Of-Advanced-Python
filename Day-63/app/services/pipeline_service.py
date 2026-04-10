import pandas as pd
from app.services.enrichment_service import enrich_data_with_external
from io import StringIO
from app.core.logger import logger
from app.core.decorators import log_execution_time

REQUIRED_COLUMNS = {"timestamp", "endpoint", "response_time", "status_code"}


def validate(df):
    logger.info("Pipeline: Validating CSV structure")

    if not REQUIRED_COLUMNS.issubset(df.columns):
        logger.error(f"Pipeline: Validation failed. Found columns: {list(df.columns)}")
        raise ValueError("Invalid CSV structure")

    logger.info("Pipeline: Validation successful")


def clean(df):
    logger.info("Pipeline: Cleaning data")

    initial_count = len(df)

    df = df[df["response_time"] >= 0]
    df = df.dropna(subset=["endpoint"])

    final_count = len(df)
    logger.info(f"Pipeline: Cleaned data | before={initial_count}, after={final_count}")

    return df


def transform(df):
    logger.info("Pipeline: Transforming data")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour

    logger.info("Pipeline: Transformation completed")
    return df


def aggregate(df):
    logger.info("Pipeline: Aggregating metrics")

    metrics = {
        "total_requests": len(df),
        "avg_latency": round(df["response_time"].mean(), 2),
        "error_rate": round((df["status_code"] >= 400).mean(), 2),
        "request_per_source": df["external_info"].value_counts().to_dict()
    }

    logger.info(
        f"Pipeline: Aggregation complete | total={metrics['total_requests']} "
        f"avg_latency={metrics['avg_latency']} error_rate={metrics['error_rate']}"
    )

    return metrics

@log_execution_time
async def process_pipeline(file):
    logger.info("Pipeline: Processing started")

    try:
        # Read file
        contents = await file.read()
        logger.info(f"Pipeline: File read complete | size={len(contents)} bytes")

        df = pd.read_csv(StringIO(contents.decode("utf-8")))
        total_records = len(df)

        logger.info(f"Pipeline: CSV loaded | total_records={total_records}")

        # Validation
        validate(df)

        # Cleaning
        df = clean(df)
        valid_records = len(df)

        # Transform
        df = transform(df)

        # Convert to dict
        records = df.to_dict(orient="records")
        logger.info(f"Pipeline: Converted to records | count={len(records)}")

        # Enrichment
        enriched_records = await enrich_data_with_external(records)

        # Back to DataFrame
        df = pd.DataFrame(enriched_records)
        logger.info("Pipeline: Enriched data converted back to DataFrame")

        # Aggregation
        metrics = aggregate(df)

        logger.info("Pipeline: Processing completed successfully")

        return {
            "total_records": total_records,
            "valid_records": valid_records,
            **metrics
        }

    except Exception as e:
        logger.exception("Pipeline: Processing failed")
        raise