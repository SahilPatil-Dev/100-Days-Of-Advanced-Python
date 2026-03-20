from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException

class UserCreate(BaseModel):
    email: EmailStr
    age: int
    
    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise HTTPException(status_code=400, detail="Age cannot be less than 18 y/o")
        return value
    
class UserResponse(BaseModel):
    email: EmailStr
    age: int