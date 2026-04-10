from app.core.cache import cache
from app.services.pipeline_service import process_pipeline
from fastapi import UploadFile
import hashlib
from app.core.logger import logger
from app.core.decorators import log_execution_time

ANALYTICS_TTL = 120  # seconds

@log_execution_time
async def get_analytics_summary(refresh: bool = False, file: UploadFile = None):
    logger.info("Analytics: Summary generation started")

    contents = await file.read()
    file_hash = hashlib.md5(contents).hexdigest()
    cache_key = f"analytics_{file_hash}"

    logger.info(f"Analytics: Generated cache key {cache_key}")

    file.file.seek(0)

    if not refresh:
        logger.info("Analytics: Checking cache")
        cached = cache.get(cache_key)

        if cached:
            logger.info("Analytics: Cache HIT")
            return {"source": "cache", "data": cached}
        else:
            logger.info("Analytics: Cache MISS")

    logger.info("Analytics: Running pipeline (fresh computation)")
    result = await process_pipeline(file)

    logger.info(f"Analytics: Storing result in cache (TTL={ANALYTICS_TTL}s)")
    cache.set(cache_key, result, ttl=ANALYTICS_TTL)

    logger.info("Analytics: Summary generation completed")
    return {"source": "computed", "data": result}