from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.permissions import require_role
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)
from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.user import UserResponseWithOrders, UserLogin, UserRegister, TokenResponse
from app.services.order_service import create_order, get_orders_by_user
from app.services.user_service import get_users_with_orders
from app.db.dependency import get_db
from app.services.user_service import register_user, login_user
from app.core.auth import get_current_user

router = APIRouter()

# Public
@router.get("/")
def read_root():
    return {"message": "API is working"}

    
@router.post("/auth/register", response_model= TokenResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, user.email, user.password, user.age)

@router.post("/auth/login", response_model= TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user.email, user.password)


# 🔒 Authenticated Routes
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    return get_user_by_id(db, user_id)

@router.get("/users/{user_id}/orders", response_model=List[OrderResponse])
def get_user_orders(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    try:
        return get_orders_by_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/orders", response_model=OrderResponse)
def create_order_endpoint(
    order: OrderCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        return create_order(db, order, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# 🔒 Authenticated + Authorized (admin) Routes

@router.delete("/users/{user_id}")
def delete_user_endpoint(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return delete_user(db, user_id)

@router.get("/users")
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    min_age: int | None = None,
    max_age: int | None = None,
    sort_by: str = "created_at",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    result = get_users(
        db=db,
        page=page,
        limit=limit,
        min_age=min_age,
        max_age=max_age,
        sort_by=sort_by,
        order=order
    )

    return {
        "data": [UserResponse.model_validate(u) for u in result["data"]],
        "page": result["page"],
        "limit": result["limit"],
        "total": result["total"]
    }

@router.post("/users", response_model=UserResponse, status_code=201)
def create_user_endpoint(
    user: UserCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return create_user(db, user)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int, 
    user: UserUpdate, 
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return update_user(db, user_id, user)

@router.get("/users-with-orders", response_model=list[UserResponseWithOrders])
def users_with_orders(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return get_users_with_orders(db)