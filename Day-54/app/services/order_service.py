from sqlalchemy.orm import Session
from app.db.models import Order, User
from app.schemas.order import OrderCreate
from fastapi import HTTPException


def create_order(db: Session, order: OrderCreate):

    user = db.query(User).filter(User.id == order.user_id).first()
    if not user:
        raise ValueError("User does not exist")

    new_order = Order(
        user_id=order.user_id,
        amount=order.amount
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return new_order


def get_orders_by_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user.orders