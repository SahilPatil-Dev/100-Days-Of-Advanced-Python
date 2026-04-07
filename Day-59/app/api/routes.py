from fastapi import UploadFile, File, HTTPException, APIRouter
from app.services.ingestion_service import handle_file_upload

router = APIRouter()

@router.post("/upload/logs")
def upload_logs(file: UploadFile = File(...)):

    try:
        result = handle_file_upload(file)

        return {
            "status": "processed",
            "total_records": result["total_records"],
            "valid_records": result["valid_records"],
            "avg_latency": result["avg_latency"],
            "error_rate": result["error_rate"]
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))