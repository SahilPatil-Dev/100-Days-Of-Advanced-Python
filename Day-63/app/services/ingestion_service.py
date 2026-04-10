from app.core.file_handler import save_uploaded_file
from app.services.pipeline_service import process_pipeline
from app.core.logger import logger
from app.core.decorators import log_execution_time

@log_execution_time
async def handle_file_upload(file):
    logger.info(f"Ingestion: Upload started for file {file.filename}")

    if not file.filename.endswith(".csv"):
        logger.error("Ingestion: Invalid file type. Only CSV allowed")
        raise ValueError("Only CSV files are allowed")

    logger.info("Ingestion: Saving file to disk")
    file_path = save_uploaded_file(file)

    logger.info(f"Ingestion: File saved at {file_path}")

    logger.info("Ingestion: Starting pipeline processing")
    result = await process_pipeline(file)

    logger.info("Ingestion: Pipeline processing completed successfully")
    return result