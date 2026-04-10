from app.integrations.external_api import fetch_external_data
from app.core.logger import logger
from app.core.decorators import log_execution_time

@log_execution_time
async def enrich_data_with_external(log_data):
    logger.info("Enrichment: Starting data enrichment")

    try:
        external_data = await fetch_external_data()
        logger.info(f"Enrichment: Retrieved {len(external_data)} external records")

        enriched = []

        for i, row in enumerate(log_data):
            row["external_info"] = external_data[i % len(external_data)]["name"]
            enriched.append(row)

        logger.info(f"Enrichment: Successfully enriched {len(enriched)} records")
        return enriched

    except Exception as e:
        logger.exception("Enrichment: Failed during enrichment process")
        raise