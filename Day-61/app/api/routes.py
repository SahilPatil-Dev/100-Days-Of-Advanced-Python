from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ingestion_service import handle_file_upload
from app.services.external_service import get_external_data

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "API is working"}

@router.get('/external-data')
async def external_data():
    return await get_external_data()

@router.post('/upload-logs')
async def upload_logs(file: UploadFile = File(...)):
    try:
        result = await handle_file_upload(file)
        
        return {
            "status": "processed",
            **result
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

