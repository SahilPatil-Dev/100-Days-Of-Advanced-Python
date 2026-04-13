from fastapi import APIRouter, status, UploadFile, File, HTTPException
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.job import JobResponse

from app.services.ingestion_service import handle_file_upload
from app.services.user_service import create_user, get_users
from app.services.order_service import create_order
from app.services.job_service import get_job_status

router = APIRouter()


# ================= USERS =================

@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
    description="Creates a new user with validated email and age"
)
def create_user_route(user: UserCreate):
    return create_user(user)


@router.get(
    "/users",
    response_model=List[UserResponse],
    summary="List users",
    description="Retrieve all users"
)
def get_users_route():
    return get_users()


# ================= ORDERS =================

@router.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create order",
    description="Create a new order for an existing user"
)
def create_order_route(order: OrderCreate):
    return create_order(order)


# ================= JOBS =================

@router.get(
    "/jobs/{job_id}",
    response_model=JobResponse,
    summary="Get job status",
    description="Fetch processing status of a background job"
)
def get_job_status_route(job_id: int):
    return get_job_status(job_id)


# ================= FILE UPLOAD =================


@router.post(
    '/upload-logs',
    summary="Upload logs",
    description="Uploads a CSV file and processes it through the analytics pipeline"
)
async def upload_logs(file: UploadFile = File(...)):
    try:
        result = await handle_file_upload(file)
        
        return {
            "status": "processed",
            **result
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
