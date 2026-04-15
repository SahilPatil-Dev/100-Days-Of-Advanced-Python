from sqlalchemy.orm import Session
from app.db.models import User


def create_user(db: Session, email: str, age: int):

    user = User(email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()