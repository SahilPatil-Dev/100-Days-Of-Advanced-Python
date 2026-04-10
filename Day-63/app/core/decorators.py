import time
import inspect
from functools import wraps
from app.core.logger import logger


def log_execution_time(func):

    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = await func(*args, **kwargs)
                duration = round(time.time() - start, 2)
                logger.info(f"{func.__name__} completed", extra={"duration": duration})
                return result
            except Exception:
                duration = round(time.time() - start, 2)
                logger.exception(f"{func.__name__} failed", extra={"duration": duration})
                raise

        return async_wrapper

    else:

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                duration = round(time.time() - start, 2)
                logger.info(f"{func.__name__} completed", extra={"duration": duration})
                return result
            except Exception:
                duration = round(time.time() - start, 2)
                logger.exception(f"{func.__name__} failed", extra={"duration": duration})
                raise

        return sync_wrapper