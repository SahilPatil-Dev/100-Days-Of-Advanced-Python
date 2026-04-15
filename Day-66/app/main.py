from fastapi import FastAPI
from app.api.routes import router
from app.db.base import Base
from app.db.session import engine
from app.core.config import setting

Base.metadata.create_all(bind=engine)

app = FastAPI(title=setting.APP_NAME)

app.include_router(router)