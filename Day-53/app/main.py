from fastapi import FastAPI
from app.api.routes import router
from app.db.session import engine
from app.db.base import Base
from app.core.config import setting

app = FastAPI(title=setting.APP_NAME)

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)