from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime, timezone

from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending")  # pending, processing, completed, failed
    file_path = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)