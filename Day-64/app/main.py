from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import AppError
from app.api.routes import router
from app.core.config import setting
from app.core.logger import logger

app = FastAPI(title=setting.APP_NAME)

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    logger.error(f"AppError: {exc.message}")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected Error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error"
        }
    )
    

app.include_router(router)