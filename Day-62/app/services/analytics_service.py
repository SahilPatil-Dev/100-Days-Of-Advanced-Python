from app.core.cache import cache
from app.services.pipeline_service import process_pipeline
from fastapi import UploadFile
import hashlib

ANALYTICS_TTL = 120  # seconds


async def get_analytics_summary(refresh: bool = False, file: UploadFile = None):
    
    contents = await file.read()
    
    file_hash = hashlib.md5(contents).hexdigest()  # unique key
    cache_key = f"analytics_{file_hash}"
    
    file.file.seek(0)

    # bypass cache if requested
    if not refresh:
        cached = cache.get(cache_key)
        if cached:
            return {"source": "cache", "data": cached}

    # compute fresh - simulate expensive work
    result = await process_pipeline(file)

    cache.set(cache_key, result, ttl=ANALYTICS_TTL)

    return {"source": "computed", "data": result}