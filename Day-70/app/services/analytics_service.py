from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.models import User, Order


def get_top_users(db: Session):

    result = (
        db.query(
            User.id,
            User.email,
            func.sum(Order.amount).label("total_spent")
        )
        .join(Order, User.id == Order.user_id)
        .group_by(User.id)
        .order_by(func.sum(Order.amount).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "user_id": r.id,
            "email": r.email,
            "total_spent": float(r.total_spent)
        }
        for r in result
    ]

