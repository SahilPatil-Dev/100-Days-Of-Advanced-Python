from fastapi import APIRouter
from app.core.config import settings
router = APIRouter()


@router.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "environment": settings.ENV
    }