import httpx
from app.core.exceptions import ExternalServiceError


async def fetch_external_data():

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://jsonplaceholder.typicode.com/users")

        if response.status_code != 200:
            raise ExternalServiceError("External API returned error")

        return response.json()

    except httpx.RequestError:
        raise ExternalServiceError("Failed to connect to external API")