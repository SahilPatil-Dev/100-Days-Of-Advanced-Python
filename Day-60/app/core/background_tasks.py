from app.services.pipeline_service import process_pipeline
from app.services.job_service import update_job_status
from app.db.session import SessionLocal
from app.db.models import Job


def process_job(job_id: int):

    db = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return

        update_job_status(db, job, "processing")

        process_pipeline(job.file_path)

        update_job_status(db, job, "completed")

    except Exception:
        if job:
            update_job_status(db, job, "failed")

    finally:
        db.close()