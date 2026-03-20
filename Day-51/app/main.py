from fastapi import FastAPI

from core.config import APP_NAME
from api.routes import router

api = FastAPI(title = APP_NAME)

api.include_router(router)