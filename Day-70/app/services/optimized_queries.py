from app.db.models import User, Order
from sqlalchemy.orm import joinedload


# BAD
def get_users_with_orders_bad(db):
    users = db.query(User).limit(10).all()

    result = []
    for user in users:
        orders = db.query(Order).filter(Order.user_id == user.id).all()
        result.append({
            "user": user.email,
            "orders": len(orders)
        })

    return result

# GOOD
def get_users_with_orders_good(db):
    users = (
        db.query(User)
        .options(joinedload(User.orders))
        .limit(10)
        .all()
    )

    return [
        {
            "user": user.email,
            "orders": len(user.orders)
        }
        for user in users
    ]

