from pydantic import BaseModel, EmailStr, Field
from fastapi import HTTPException

class UserCreate(BaseModel):
    email: EmailStr
    age: int = Field(..., ge=18, description="Age must be at least 18")

    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int

    class Config:
        form_attributes = True # This allows to return Objects in ORM Models