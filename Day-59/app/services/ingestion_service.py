from app.core.file_handler import save_uploaded_file
from app.services.pipeline_service import process_pipeline


def handle_file_upload(file):

    if not file.filename.endswith(".csv"):
        raise ValueError("Only CSV files are allowed")

    file_path = save_uploaded_file(file)

    result = process_pipeline(file_path)

    return result