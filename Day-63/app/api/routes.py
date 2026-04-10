from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ingestion_service import handle_file_upload
from app.services.external_service import get_external_data
from app.services.analytics_service import get_analytics_summary
from app.core.logger import logger

router = APIRouter()

@router.get("/")
def read_root():
    logger.info("GET / - Health check endpoint hit")
    return {"message": "API is working"}

@router.get('/external-data')
async def external_data():
    logger.info("GET /external-data - Request received")
    try:
        data = await get_external_data()
        logger.info("GET /external-data - Response sent successfully")
        return data
    except Exception as e:
        logger.exception("GET /external-data - Failed to fetch data")
        raise HTTPException(status_code=500, detail="Failed to fetch external data")

@router.post('/upload-logs')
async def upload_logs(file: UploadFile = File(...)):
    logger.info(f"POST /upload-logs - File received: {file.filename}")
    try:
        result = await handle_file_upload(file)
        logger.info("POST /upload-logs - File processed successfully")
        return {"status": "processed", **result}
    except Exception as e:
        logger.exception("POST /upload-logs - Processing failed")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/analytics/summary")
async def analytics_summary(refresh: bool = False, file: UploadFile = File(...)):
    logger.info(f"POST /analytics/summary - Request received | refresh={refresh}")
    try:
        result = await get_analytics_summary(refresh, file)
        logger.info("POST /analytics/summary - Summary generated successfully")
        return {"status": "processed", **result}
    except Exception as e:
        logger.exception("POST /analytics/summary - Failed")
        raise HTTPException(status_code=400, detail=str(e))