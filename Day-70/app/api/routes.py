from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.analytics_service import get_top_users
from app.services.optimized_queries import (
    get_users_with_orders_bad,
    get_users_with_orders_good,
)

router = APIRouter()


# Health check
@router.get("/")
def root():
    return {"status": "running"}


# Analytics endpoint
@router.get("/analytics/top-users")
def top_users(db: Session = Depends(get_db)):
    return get_top_users(db)


# N+1 BAD (for testing)
@router.get("/users-with-orders/bad")
def users_bad(db: Session = Depends(get_db)):
    return get_users_with_orders_bad(db)


# N+1 GOOD (optimized)
@router.get("/users-with-orders/good")
def users_good(db: Session = Depends(get_db)):
    return get_users_with_orders_good(db)

