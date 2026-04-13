from fastapi import APIRouter
from pydantic import EmailStr
from app.services.user_service import create_user, get_user
from app.integration.external_api import fetch_external_data
router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "API is working"}


@router.post("/users")
def create_user_endpoint(email: EmailStr, age: int):
    return create_user(email, age)

@router.get('/user')
def get_users(user_id: int):
    return get_user(user_id)

@router.get('/external-data')
async def fetch_data():
    data = await fetch_external_data()
    return data
