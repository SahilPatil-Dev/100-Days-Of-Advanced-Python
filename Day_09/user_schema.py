class ValidationError(Exception):
    pass


class InvalidEmailError(ValidationError):
    pass


class InvalidAgeError(ValidationError):
    pass


class User:
    def __init__(self, email, age):
        self.email = email
        self.age = age

    @classmethod
    def from_dict(cls, data):
        email = data.get("email")
        age = data.get("age")

        # Email validation
        if not isinstance(email, str) or "@" not in email:
            raise InvalidEmailError("Invalid email")
        
        local, domain = email.split("@", 1)
        if not local or not domain:
            raise InvalidEmailError("Invalid email")

        # Age validation
        try:
            if not isinstance(age, (int, str)):
                raise InvalidAgeError("Age must be a Number")
            age = int(age)
        except (TypeError, ValueError):
            raise InvalidAgeError("Age must be a number")


        if age < 18:
            raise InvalidAgeError("Age must be 18 or older")

        return cls(email=email.lower(), age=age)


if __name__ == "__main__":
    try:
        user = User.from_dict({
            "email": "TEST@Email.com",
            "age": "25"
        })

        print("User created successfully!")
        print("Email:", user.email)
        print("Age:", user.age)

    except ValidationError as e:
        print("Error:", e)
