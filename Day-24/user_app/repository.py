from typing import List
from schemas import User


class UserRepository:
    def __init__(self):
        self._users: List[User] = []
        self._id_counter = 1

    def save(self, email: str, age: int) -> User:
        user = User(
            id=self._id_counter,
            email=email,
            age=age
        )
        self._users.append(user)
        self._id_counter += 1
        return user

    def get_all(self) -> List[User]:
        return list(self._users)
