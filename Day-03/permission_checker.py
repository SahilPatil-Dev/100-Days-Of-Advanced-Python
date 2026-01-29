def permission_required(role):
    def check(user_role):
        return user_role == role
    return check


admin_check = permission_required("admin")
user_check = permission_required("user")

print(admin_check("admin"))   # True
print(admin_check("user"))    # False
print(user_check("user"))     # True
print(user_check("admin"))    # False
