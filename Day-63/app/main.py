from fastapi import FastAPI, Request
from app.api.routes import router
from app.core.config import setting
from app.db.session import engine
from app.db.base import Base
from app.core.request_context import set_request_id

app = FastAPI(title=setting.APP_NAME)

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = set_request_id()

    response = await call_next(request)
    
    response.headers["X-Request-ID"] = request_id

    return response

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)