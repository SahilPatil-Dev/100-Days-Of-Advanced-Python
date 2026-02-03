from pathlib import Path
import json

new_user = {
    "user": "Sahil"
}

def append_user():
    data_path = Path(__file__).parent / "users.json"

    # If file doesn't exist, start with empty list
    if data_path.exists():
        with data_path.open("r", encoding="utf-8") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    # Append new user
    users.append(new_user)

    # Write back updated data
    with data_path.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    return users


if __name__ == "__main__":
    updated_users = append_user()
    print(updated_users)
