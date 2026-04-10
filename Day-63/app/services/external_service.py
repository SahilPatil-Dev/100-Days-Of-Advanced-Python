from app.integrations.external_api import fetch_external_data, ExternalAPIError
from app.core.logger import logger
from app.core.decorators import log_execution_time

@log_execution_time
async def get_external_data():
    logger.info("Service: Fetching external data")

    try:
        data = await fetch_external_data()
        logger.info(f"Service: Retrieved {len(data)} records from external API")

        return {
            "status": "Success",
            "count": len(data),
            "data": data[:5]
        }

    except ExternalAPIError as e:
        logger.error(f"Service: External API error - {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }