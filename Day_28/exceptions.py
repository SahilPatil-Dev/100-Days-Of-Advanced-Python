class AppError(Exception):
    """Base application-level exception."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ValidationError(AppError):
    """Raised when input validation fails."""
    pass


class NotFoundError(AppError):
    """Raised when a requested entity does not exist."""
    pass


class InfrastructureError(AppError):
    """Raised when infrastructure (DB, network, file system) fails."""
    pass
