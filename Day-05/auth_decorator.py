def require_role(role : list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_role = args[0]  # simplified assumption

            if user_role not in role:
                return "Access denied"

            return func(*args, **kwargs)

        return wrapper
    return decorator


@require_role(["admin", "manager"])
def delete_user(user_role, name):
    return f"{user_role} deleted {name}"


# Example runs
print(delete_user("admin", "Sahil"))  # User deleted
print(delete_user("manager", "Sahil"))  # User deleted
print(delete_user("user", "Sahil"))   # Access denied
