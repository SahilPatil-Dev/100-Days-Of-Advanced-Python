from app.integrations.external_api import fetch_external_data, ExternalAPIError

async def get_external_data():
    
    try:
        data = await fetch_external_data()

        return {
            "status": "Success",
            "count": len(data),
            "data": data[:5]
        }
    
    except ExternalAPIError as e:

        return {
            "status": "error",
            "message": str(e)
        }