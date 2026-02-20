# Buggy Version (Unintended Mutation)
# def update_user_role(user: dict, new_role: str):
#     # Directly mutates input dictionary
#     user["role"] = new_role
#     return user


# if __name__ == "__main__":
#     original_user = {"id": 1, "name": "Sahil", "role": "user"}

#     updated_user = update_user_role(original_user, "admin")

#     print("Updated:", updated_user)
#     print("Original:", original_user)  # Unexpected mutation


# Fixed Version (Defensive Copy)
import copy


def update_user_role_safe(user: dict, new_role: str):
    user_copy = user.copy()  # shallow copy
    user_copy["role"] = new_role
    return user_copy


if __name__ == "__main__":
    original_user = {"id": 1, "name": "Sahil", "role": "user"}

    updated_user = update_user_role_safe(original_user, "admin")

    print("Updated:", updated_user)
    print("Original:", original_user)  # Remains unchanged
