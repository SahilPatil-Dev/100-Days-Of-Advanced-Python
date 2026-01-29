def is_long_enough(value):
    return len(value) >= 5

def is_numeric(value):
    return value.isdigit()

def is_email(value):
    return "@" in value and "." in value


validators = [is_long_enough, is_email, is_numeric]


def validate_input(value):
    for validator in validators:
        if not validator(value):
            return False
    return True


print(validate_input("test@email.com"))
print(validate_input("123"))
