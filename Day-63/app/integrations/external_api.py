import httpx
from app.core.cache import cache
from app.core.logger import logger
from app.core.decorators import log_execution_time

CACHE_KEY = "external_users"
CACHE_TTL = 60  # seconds

class ExternalAPIError(Exception):
    pass

@log_execution_time
async def fetch_external_data():
    logger.info("External API: Checking cache")

    cached_data = cache.get(CACHE_KEY)
    if cached_data:
        logger.info("External API: Cache HIT")
        return cached_data

    logger.info("External API: Cache MISS → Calling API")

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)

        logger.info(f"External API: Response status {response.status_code}")

        if response.status_code != 200:
            logger.error("External API: Non-200 response")
            raise ExternalAPIError("External API failed")

        data = response.json()

        logger.info("External API: Caching response")
        cache.set(CACHE_KEY, data, ttl=CACHE_TTL)

        return data

    except httpx.RequestError as e:
        logger.exception("External API: Request failed")
        raise ExternalAPIError("Connection failed")