from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_users
from app.db.session import SessionLocal
from app.db.dependency import get_db

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "API is working"}

@router.post("/users", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):

    try:
        new_user = create_user(db, user)
        return new_user

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=List[UserResponse])
def list_users(
    min_age: int = Query(None),
    db: Session = Depends(get_db)
):
    users = get_users(db, min_age)
    return users