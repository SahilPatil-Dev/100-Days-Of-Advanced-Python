from pydantic import BaseModel
from datetime import datetime

class JobResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    completed_at: datetime | None

    class Config:
        from_attributes = True 