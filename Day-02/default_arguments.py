"""
Day 2 – Mutability Traps & Default Arguments
"""

# ---------- BAD PRACTICE ----------
def add_item_bad(item, items=[]):
    items.append(item)
    return items


print(add_item_bad(1))
print(add_item_bad(2))
print(add_item_bad(3))

print("-" * 50)

# ---------- GOOD PRACTICE ----------
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_good(1))
print(add_item_good(2))
print(add_item_good(3))

print("-" * 50)

# ---------- CLASS TRAP ----------
class UserBad:
    def __init__(self, roles=[]):
        self.roles = roles


u1 = UserBad()
u2 = UserBad()

u1.roles.append("admin")
u2.roles.append("editor")

print("User 1 roles:", u1.roles)
print("User 2 roles:", u2.roles)

print("-" * 50)

# ---------- GOOD PRACTICE ----------
class User:
    def __init__(self, roles=None):
        self.roles = roles if roles is not None else []

u1 = User()
u2 = User()

u1.roles.append("admin")
u2.roles.append("editor")

print("User 1 roles:", u1.roles)
print("User 2 roles:", u2.roles)
