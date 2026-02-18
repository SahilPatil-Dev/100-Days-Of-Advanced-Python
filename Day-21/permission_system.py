import time


def check_permission_list(user_roles, required_role):
    return required_role in user_roles


def check_permission_set(user_roles, required_role):
    return required_role in user_roles


def benchmark():
    roles = [f"role_{i}" for i in range(100_000)]
    required = "role_99999"

    roles_list = roles
    roles_set = set(roles)

    # List check
    start = time.perf_counter()
    check_permission_list(roles_list, required)
    list_time = time.perf_counter() - start

    # Set check
    start = time.perf_counter()
    check_permission_set(roles_set, required)
    set_time = time.perf_counter() - start

    print(f"List permission check: {list_time:.8f}")
    print(f"Set permission check:  {set_time:.8f}")


if __name__ == "__main__":
    benchmark()
