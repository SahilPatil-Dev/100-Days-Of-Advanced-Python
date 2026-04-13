# app/schemas/job.py

from pydantic import BaseModel, Field


class JobResponse(BaseModel):
    job_id: int = Field(..., example=1)
    status: str = Field(
        ...,
        description="Job status",
        example="completed"
    )