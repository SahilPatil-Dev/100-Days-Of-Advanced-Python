from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from fastapi import HTTPException
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    age: int = Field(..., ge=18)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18)
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int

    class Config:
        from_attributes = True # This allows to return Objects in ORM Models
        
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
    orders: List[OrderNested] = Field(default_factory=list)

    class Config:
        from_attributes = True
        
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    age: int = Field(..., ge=18)
    
class UserLogin(BaseModel):
    email:EmailStr
    password: str
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    role: str