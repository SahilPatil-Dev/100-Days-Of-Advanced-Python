from repository import UserRepository
from service import UserService
from validators import ValidationError

repository = UserRepository()
service = UserService(repository)

def main():
    users_data = [
        {"email": "SAhil@Example.com", "age": 25},
        {"email": "Rahul@Example.com", "age": 23},
        {"email": "Satish@Gmail.com", "age": 45}
    ]

    for data in users_data:
        try:
            user = service.create_user(data)

            print({
                "success": True,
                "data": user
            })

        except ValidationError as e:
            print({
                "success": False,
                "error": str(e)
            })

    print("\nAll Users in Repository:")
    print(repository.get_all())


if __name__ == "__main__":
    main()
