from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from fastapi import HTTPException
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    age: int = Field(..., ge=18, description="Age must be at least 18")

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18)
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int

    class Config:
        form_attributes = True # This allows to return Objects in ORM Models
        
class OrderNested(BaseModel):
    id: int
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponseWithOrders(BaseModel):
    id: int
    email: EmailStr
    age: int
    orders: List[OrderNested] = []

    class Config:
        from_attributes = True