import httpx

class ExternalAPIError(Exception):
    pass


async def fetch_external_data():
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
        
        if response.status_code != 200:
            raise ExternalAPIError("External API returned non-200 response")
        
        return response.json()
    
    except httpx.RequestError:
        raise ExternalAPIError("Failed to connect to the External API")
    
    except Exception as e:
        raise ExternalAPIError(f"Unexpected error while calling external API {e}")
    
    