from response_formatter import success_response, error_response


def handle_get_users():
    return success_response(
        data=[{"id": 1, "email": "user@example.com", "age": 25}]
    )


def handle_get_user(user_id: int):
    if user_id != 1:
        return error_response("User not found", 404)

    return success_response(
        data={"id": 1, "email": "user@example.com", "age": 25}
    )


def route_request(method: str, path: str):
    if method == "GET" and path == "/users":
        return handle_get_users()

    if method == "GET" and path.startswith("/users/"):
        try:
            user_id = int(path.split("/")[-1])
        except ValueError:
            return error_response("Invalid user ID", 400)

        return handle_get_user(user_id)

    return error_response("Route not found", 404)


if __name__ == "__main__":
    print(route_request("GET", "/users"))
    print(route_request("GET", "/users/1"))
    print(route_request("GET", "/users/ABC"))
    print(route_request("GET", "/users/999"))
    print(route_request("GET", "/invalid"))
