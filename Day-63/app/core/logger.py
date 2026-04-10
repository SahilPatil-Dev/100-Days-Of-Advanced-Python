import logging
import json
from app.core.request_context import get_request_id

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "request_id": get_request_id()
        }
        
        if hasattr(record, "duration"):
            log_record["duration"] = record.duration

        if hasattr(record, "status"):
            log_record["status"] = record.status
        
        return json.dumps(log_record)

def setup_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = JsonFormatter()
        
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()