import requests
from typing import Dict, Any


class APIClientError(Exception):
    pass


class UserAPIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    def __init__(self, timeout: int = 5) -> None:
        self.timeout = timeout

    def get_user(self, user_id: int) -> Dict[str, Any]:
        try:
            response = requests.get(
                f"{self.BASE_URL}/{user_id}",
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise APIClientError(f"Network failure: {e}")

        if response.status_code != 200:
            raise APIClientError(
                f"Failed with status {response.status_code}"
            )

        try:
            data = response.json()
        except ValueError:
            raise APIClientError("Invalid JSON returned")

        return {
            "id": data.get("id"),
            "name": data.get("name"),
            "email": data.get("email"),
        }

    def create_user(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            response = requests.post(
                self.BASE_URL,
                json=payload,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise APIClientError(f"Network failure: {e}")

        if response.status_code not in (200, 201):
            raise APIClientError(
                f"User creation failed with status {response.status_code}"
            )

        try:
            return response.json()
        except ValueError:
            raise APIClientError("Invalid JSON returned")


if __name__ == "__main__":
    client = UserAPIClient()

    user = client.get_user(1)
    print("Fetched:", user)

    new_user = client.create_user({
        "name": "Test User",
        "email": "test@example.com"
    })
    print("Created:", new_user)
