jobs_db = {
    1: "completed",
    2: "processing"
}


def get_job_status(job_id: int):

    status = jobs_db.get(job_id, "not_found")

    return {
        "job_id": job_id,
        "status": status
    }