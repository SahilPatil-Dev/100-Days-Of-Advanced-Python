from sqlalchemy.orm import Session
from app.db.models import Job
from datetime import datetime, timezone
from fastapi import HTTPException


def create_job(db: Session, file_path: str):
    job = Job(file_path=file_path, status="pending")
    try:
        db.add(job)
        db.commit()
        db.refresh(job)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return job


def get_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def update_job_status(db: Session, job: Job, status: str):
    job.status = status
    if status in ["completed", "failed"]:
        job.completed_at = datetime.now(timezone.utc)
    try:
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))