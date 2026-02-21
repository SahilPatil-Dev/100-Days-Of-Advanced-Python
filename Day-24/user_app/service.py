from validators import validate_user_input
from repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, data: dict):
        validate_user_input(data)

        email = data["email"].lower()
        age = int(data["age"])

        return self.repository.save(email, age)
