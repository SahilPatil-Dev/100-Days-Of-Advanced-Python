def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Args: {args} & kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(5, 7))