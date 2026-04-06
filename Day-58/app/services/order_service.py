from sqlalchemy.orm import Session
from app.db.models import Order, User
from app.schemas.order import OrderCreate
from fastapi import HTTPException
from datetime import datetime, timezone


def create_order(db: Session, user_id: int, amount: float):

    if amount <= 0:
        raise ValueError("Amount must be positive")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")

    order = Order(
        user_id=user_id,
        amount=amount,
        created_at=datetime.now(timezone.utc)
    )

    try:
        db.add(order)
        db.commit()
        db.refresh(order)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return order


def get_orders_by_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user.orders