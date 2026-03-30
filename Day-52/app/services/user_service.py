from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):

    # check duplicate email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("Email already exists")

    new_user = User(
        email=user.email,
        age=user.age
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return new_user


def get_users(db: Session, min_age: int = None):
    
    query = db.query(User)

    if min_age:
        query = query.filter(User.age >= min_age)

    return query.all()