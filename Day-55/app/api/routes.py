from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)
from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.user import UserResponseWithOrders
from app.services.order_service import create_order, get_orders_by_user
from app.services.user_service import get_users_with_orders
from app.db.dependency import get_db
from app.schemas.user import UserRegister, UserLogin
from app.services.user_service import register_user, login_user
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "API is working"}


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)




@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)


@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

@router.post("/orders", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        return create_order(db, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/users/{user_id}/orders", response_model=list[OrderResponse])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_orders_by_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/users-with-orders", response_model=list[UserResponseWithOrders])
def users_with_orders(db: Session = Depends(get_db)):
    return get_users_with_orders(db)

@router.post("/auth/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        return register_user(db, user.email, user.password, user.age)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user(db, user.email, user.password)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# 🔒 Protect Routes
@router.post("/orders")
def create_order_endpoint(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_order(db, order)


@router.get("/users", response_model=List[UserResponse])
def list_users(
    min_age: int = Query(None),
    max_age: int = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_users(db, min_age, max_age)