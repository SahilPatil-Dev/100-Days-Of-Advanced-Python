# app/schemas/user.py

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr = Field(
        ...,
        description="User's email address",
        example="user@example.com"
    )
    age: int = Field(
        ...,
        ge=18,
        description="User's age (must be 18 or older)",
        example=25
    )


class UserResponse(BaseModel):
    id: int = Field(..., example=1)
    email: EmailStr = Field(..., example="user@example.com")
    age: int = Field(..., example=25)

    class Config:
        from_attributes = True