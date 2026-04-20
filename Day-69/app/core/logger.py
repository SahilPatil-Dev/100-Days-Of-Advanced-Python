import logging
from app.core.config import settings

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)