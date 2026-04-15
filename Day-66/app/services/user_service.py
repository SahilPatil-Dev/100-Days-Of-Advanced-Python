from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.core.exceptions import NotFoundError


def create_user(db: Session, user_data):

    return user_repository.create_user(
        db,
        email=user_data.email,
        age=user_data.age
    )


def get_users(db: Session):
    return user_repository.get_users(db)


def get_user_by_id(db: Session, user_id: int):

    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise NotFoundError("User not found")

    return user