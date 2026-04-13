# app/schemas/order.py

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    user_id: int = Field(
        ...,
        description="ID of the user placing the order",
        example=1
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Order amount (must be positive)",
        example=250.75
    )


class OrderResponse(BaseModel):
    id: int = Field(..., example=1)
    user_id: int = Field(..., example=1)
    amount: float = Field(..., example=250.75)

    class Config:
        from_attributes = True