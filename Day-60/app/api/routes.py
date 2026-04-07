from fastapi import UploadFile, File, HTTPException, APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from app.services.job_service import create_job, get_job
from app.core.file_handler import save_uploaded_file
from app.core.background_tasks import process_job
from app.db.dependency import get_db
from app.schemas.jobs import JobResponse

router = APIRouter()



@router.post("/upload/logs", response_model= JobResponse, response_model_exclude_none= True)
def upload_logs(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    file_path = save_uploaded_file(file)

    job = create_job(db, file_path)

    background_tasks.add_task(process_job, job.id)

    return job
    
@router.get("/jobs/{job_id}", response_model= JobResponse, response_model_exclude_none= True)
def get_job_status(job_id: int, db: Session = Depends(get_db)):

    job = get_job(db, job_id)

    return job