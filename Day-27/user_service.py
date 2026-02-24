from repository_interface import (
    UserRepository,
    User,
    InMemoryUserRepository,
    MockUserRepository
)


class UserService:

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create_user(self, user_id: int, email: str) -> User:
        user = User(id=user_id, email=email)
        self._repository.save(user)
        return user

    def get_user(self, user_id: int):
        return self._repository.get_by_id(user_id)


if __name__ == "__main__":

    print("---- Using REAL Repository ----")
    real_repo = InMemoryUserRepository()
    service_real = UserService(real_repo)

    service_real.create_user(1, "real@example.com")
    user = service_real.get_user(1)
    print("Fetched from real repo:", user)

    print("\n---- Using MOCK Repository ----")
    mock_repo = MockUserRepository()
    service_mock = UserService(mock_repo)

    service_mock.create_user(2, "mock@example.com")
    user = service_mock.get_user(2)
    print("Fetched from mock repo:", user)