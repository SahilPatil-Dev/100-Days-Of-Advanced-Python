from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.db.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password, verify_password, create_access_token


def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password),
        age=user.age,
        role="user"
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return new_user


def get_users(db: Session, min_age: int = None, max_age: int = None):
    
    if min_age is not None and max_age is not None and min_age > max_age:
        raise HTTPException(status_code=400, detail="min_age cannot be greater than max_age")

    query = db.query(User)

    if min_age is not None:
        query = query.filter(User.age >= min_age)

    if max_age is not None:
        query = query.filter(User.age <= max_age)

    return query.all()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")


    if user_data.email is not None:
        
        existing = db.query(User).filter(
            User.email == user_data.email,
            User.id != user_id
        ).first()
        
        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")
        user.email = user_data.email

    if user_data.age is not None:
        user.age = user_data.age

    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        db.delete(user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return {"message": "User deleted successfully"}

def get_users_with_orders(db: Session):
    return db.query(User).options(joinedload(User.orders)).all()

def register_user(db: Session, email: str, password: str, age: int):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")
    
    user = User(
        email = email,
        password_hash = hash_password(password),
        age = age,
        role = "user"
    )
    
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "role": user.role
    }