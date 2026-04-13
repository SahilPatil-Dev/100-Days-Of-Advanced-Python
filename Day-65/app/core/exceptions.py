class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ValidationError(AppError):
    def __init__(self, message="Invalid input"):
        super().__init__(message, status_code=422)


class NotFoundError(AppError):
    def __init__(self, message="Resource not found"):
        super().__init__(message, status_code=404)


class UnauthorizedError(AppError):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, status_code=401)


class ExternalServiceError(AppError):
    def __init__(self, message="External service failed"):
        super().__init__(message, status_code=502)