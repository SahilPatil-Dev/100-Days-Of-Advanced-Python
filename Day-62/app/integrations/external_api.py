import httpx
from app.core.cache import cache

CACHE_KEY = "external_users"
CACHE_TTL = 60  # seconds


class ExternalAPIError(Exception):
    pass


async def fetch_external_data():

    # Step 1: Check cache
    cached_data = cache.get(CACHE_KEY)
    if cached_data:
        return cached_data

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)

        if response.status_code != 200:
            raise ExternalAPIError("External API failed")

        data = response.json()

        # Step 2: Store in cache
        cache.set(CACHE_KEY, data, ttl=CACHE_TTL)

        return data

    except httpx.RequestError:
        raise ExternalAPIError("Connection failed")