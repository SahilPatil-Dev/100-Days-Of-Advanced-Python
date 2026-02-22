from validators import normalize_user_input


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, data: dict):
        normalized = normalize_user_input(data)
        return self.repository.save(
            normalized["email"],
            normalized["age"]
        )