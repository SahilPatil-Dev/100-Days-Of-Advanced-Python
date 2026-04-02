from pydantic import BaseModel, Field
from datetime import datetime


class OrderCreate(BaseModel):
    user_id: int
    amount: float = Field(..., gt=0)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True