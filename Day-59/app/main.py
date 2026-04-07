from fastapi import FastAPI
from app.api.routes import router

APP_NAME = "Pipeline Processing"

app = FastAPI(title=APP_NAME)

app.include_router(router)