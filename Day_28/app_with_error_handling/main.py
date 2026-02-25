from .repository import UserRepository
from .service import UserService
from ..exceptions import AppError
from ..error_handler import handle_exception


def main():
    repo = UserRepository()
    service = UserService(repo)

    try:
        service.create_user(1, "invalid-email")  # triggers ValidationError
    except AppError as e:
        response = handle_exception(e)
        print(response)


if __name__ == "__main__":
    main()
