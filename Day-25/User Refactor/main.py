from repository import UserRepository
from service import UserService
from validators import ValidationError


def main():
    repository = UserRepository()
    service = UserService(repository)

    users = [
        {"email": "Test@Example.com", "age": "25"},
        {"email": "Rahul@Example.com", "age": "22"}
    ]

    for user_data in users:
        try:
            user = service.create_user(user_data)
            print("Created:", user)
        except ValidationError as e:
            print("Error:", str(e))

    print("\nAll Users:", repository.get_all())


if __name__ == "__main__":
    main()