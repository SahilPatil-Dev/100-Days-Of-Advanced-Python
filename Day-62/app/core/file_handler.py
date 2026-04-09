import os
from uuid import uuid4

UPLOAD_DIR = "uploads"


def save_uploaded_file(file):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    file_extension = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{file_extension}"

    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as f:
        while chunk := file.file.read(1024 * 1024):  # 1MB chunks
            f.write(chunk)
            
    file.file.seek(0)

    return file_path