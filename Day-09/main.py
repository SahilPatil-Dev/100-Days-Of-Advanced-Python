from user_schema import User
from serializer import serialize_user

user = User.from_dict({
    "email": "TEST@Email.com",
    "age": "30"
})

if __name__ == "__main__":
    response = serialize_user(user)

    print(response)
