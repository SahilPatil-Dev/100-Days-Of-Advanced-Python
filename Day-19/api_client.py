import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_user(user_id: int) -> dict:
    try:
        response = requests.get(f"{API_URL}/{user_id}", timeout=5)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Unexpected status code: {response.status_code}"
        )

    try:
        data = response.json()
    except ValueError:
        raise RuntimeError("Failed to parse JSON response")

    if "id" not in data or "email" not in data:
        raise RuntimeError("Invalid response structure")

    return data


if __name__ == "__main__":
    user = fetch_user(1)
    print(user)
