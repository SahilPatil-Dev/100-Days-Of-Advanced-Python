from fastapi import APIRouter, Depends, Query, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.permissions import require_role
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.schemas.order import OrderCreate
from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)
from app.schemas.order import OrderResponse
from app.schemas.user import UserResponseWithOrders, UserLogin, UserRegister, TokenResponse
from app.services.order_service import create_order, get_orders_by_user
from app.services.user_service import get_users_with_orders
from app.db.dependency import get_db
from app.services.user_service import register_user, login_user
from app.core.auth import get_current_user
from app.core.background_tasks import log_order_creation
from app.core.logger import logger

router = APIRouter()


# Public
@router.get("/")
def read_root():
    logger.info("GET / - Request received")
    return {"message": "API is working"}


@router.post("/auth/register", response_model=TokenResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    logger.info(f"POST /auth/register - Register attempt for email={user.email}")
    result = register_user(db, user.email, user.password, user.age)
    logger.info(f"POST /auth/register - Registration successful for email={user.email}")
    return result


@router.post("/auth/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    logger.info(f"POST /auth/login - Login attempt for email={user.email}")
    result = login_user(db, user.email, user.password)
    logger.info(f"POST /auth/login - Login successful for email={user.email}")
    return result


# Authenticated Routes
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(f"GET /users/{user_id} - Requested by user_id={current_user.id}")

    if current_user.id != user_id and current_user.role != "admin":
        logger.warning(
            f"GET /users/{user_id} - Unauthorized access attempt by user_id={current_user.id}"
        )
        raise HTTPException(status_code=403, detail="Not authorized")

    result = get_user_by_id(db, user_id)
    logger.info(f"GET /users/{user_id} - User fetched successfully")
    return result


@router.get("/users/{user_id}/orders", response_model=List[OrderResponse])
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(
        f"GET /users/{user_id}/orders - Requested by user_id={current_user.id}"
    )

    if current_user.id != user_id and current_user.role != "admin":
        logger.warning(
            f"GET /users/{user_id}/orders - Unauthorized access attempt by user_id={current_user.id}"
        )
        raise HTTPException(status_code=403, detail="Not authorized")

    try:
        result = get_orders_by_user(db, user_id)
        logger.info(f"GET /users/{user_id}/orders - Orders fetched successfully")
        return result
    except ValueError as e:
        logger.error(f"GET /users/{user_id}/orders - {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/orders", response_model=OrderResponse)
def create_order_endpoint(
    background_tasks: BackgroundTasks,
    amount: float = Query(..., gt=0),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    logger.info(
        f"POST /orders - Order creation requested by user_id={current_user.id}, amount={amount}"
    )

    order = create_order(
        db,
        OrderCreate(amount=amount),
        current_user.id
    )

    background_tasks.add_task(
        log_order_creation,
        order.id,
        current_user.id
    )

    logger.info(
        f"POST /orders - Order created successfully order_id={order.id}, user_id={current_user.id}"
    )

    return order


# Authenticated + Authorized (admin) Routes
@router.delete("/users/{user_id}")
def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("admin"))
):
    logger.info(
        f"DELETE /users/{user_id} - Requested by admin user_id={current_user.id}"
    )

    result = delete_user(db, user_id)

    logger.info(f"DELETE /users/{user_id} - User deleted successfully")
    return result


@router.get("/users")
async def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    min_age: int | None = None,
    max_age: int | None = None,
    sort_by: str = "created_at",
    order: str = "asc",
    db: Session = Depends(get_db),
    current_user=Depends(require_role("admin"))
):
    logger.info(
        f"GET /users - Requested by admin user_id={current_user.id}, "
        f"page={page}, limit={limit}, min_age={min_age}, max_age={max_age}, "
        f"sort_by={sort_by}, order={order}"
    )

    result = get_users(
        db=db,
        page=page,
        limit=limit,
        min_age=min_age,
        max_age=max_age,
        sort_by=sort_by,
        order=order
    )

    logger.info(
        f"GET /users - Retrieved {len(result['data'])} users successfully"
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
    current_user=Depends(require_role("admin"))
):
    logger.info(
        f"POST /users - Admin user_id={current_user.id} creating user email={user.email}"
    )

    result = create_user(db, user)

    logger.info(f"POST /users - User created successfully email={user.email}")
    return result


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("admin"))
):
    logger.info(
        f"PUT /users/{user_id} - Requested by admin user_id={current_user.id}"
    )

    result = update_user(db, user_id, user)

    logger.info(f"PUT /users/{user_id} - User updated successfully")
    return result


@router.get("/users-with-orders", response_model=list[UserResponseWithOrders])
def users_with_orders(
    db: Session = Depends(get_db),
    current_user=Depends(require_role("admin"))
):
    logger.info(
        f"GET /users-with-orders - Requested by admin user_id={current_user.id}"
    )

    result = get_users_with_orders(db)

    logger.info(
        f"GET /users-with-orders - Retrieved {len(result)} users with orders"
    )

    return result