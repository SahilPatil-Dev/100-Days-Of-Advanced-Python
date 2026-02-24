from abc import ABC, abstractmethod
from typing import Dict, Optional
from dataclasses import dataclass


# Simple domain model
@dataclass
class User:
    id: int
    email: str


# Abstraction (Interface)
class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass


# Concrete implementation (Production-like)
class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self._storage: Dict[int, User] = {}

    def save(self, user: User) -> None:
        self._storage[user.id] = user
        print(f"[REAL] Saved user {user.id}")

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._storage.get(user_id)


# Mock implementation (Testing)
class MockUserRepository(UserRepository):

    def save(self, user: User) -> None:
        print(f"[MOCK] Pretending to save user {user.id}")

    def get_by_id(self, user_id: int) -> Optional[User]:
        print(f"[MOCK] Pretending to fetch user {user_id}")
        return None