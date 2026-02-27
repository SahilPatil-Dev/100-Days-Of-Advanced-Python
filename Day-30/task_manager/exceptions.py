class AppError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ValidationError(AppError):
    pass


class NotFoundError(AppError):
    pass


class InfrastructureError(AppError):
    pass
