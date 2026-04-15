from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)