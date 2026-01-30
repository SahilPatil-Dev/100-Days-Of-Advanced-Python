def allowed_roles(roles: list):
    def check(user_role):
        return user_role in roles
    return check


admin_only = allowed_roles(["admin"])
print(admin_only("user"))   # False
print(admin_only("admin"))  # True
