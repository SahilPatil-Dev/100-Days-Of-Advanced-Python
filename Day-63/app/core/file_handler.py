import os
from uuid import uuid4
from app.core.logger import logger

UPLOAD_DIR = "uploads"

def save_uploaded_file(file):
    logger.info("FileHandler: Saving uploaded file")

    if not os.path.exists(UPLOAD_DIR):
        logger.info(f"FileHandler: Directory '{UPLOAD_DIR}' not found → Creating")
        os.makedirs(UPLOAD_DIR)
    else:
        logger.info(f"FileHandler: Directory '{UPLOAD_DIR}' already exists")

    file_extension = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{file_extension}"

    file_path = os.path.join(UPLOAD_DIR, unique_name)

    logger.info(f"FileHandler: Writing file to {file_path}")

    with open(file_path, "wb") as f:
        while chunk := file.file.read(1024 * 1024):
            f.write(chunk)

    file.file.seek(0)

    logger.info("FileHandler: File saved successfully")
    return file_path