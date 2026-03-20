from fastapi import APIRouter, Query
from typing import List

from schemas.user import UserCreate, UserResponse
from services.user_service import create_user, get_user

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user_endpoint(user: UserCreate):
    
    result = create_user(user)

    return result

@router.get("/users", response_model=List[UserResponse])
def get_user_endpoint(min_age: int = Query(None)):
    
    result = get_user(min_age)
    
    return result