from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Backend Analytics API",
    description="Production-style backend with clean architecture and documentation",
    version="1.0.0"
)

app.include_router(router)