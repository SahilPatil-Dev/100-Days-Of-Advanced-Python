def rate_limiter(limit):
    count = 0

    def check():
        nonlocal count
        if count >= limit:
            return "Rate limit exceeded"
        count += 1
        return "Allowed"

    return check


limit_3 = rate_limiter(3)
print(limit_3())  # allowed
print(limit_3())  # allowed
print(limit_3())  # allowed
print(limit_3())  # blocked
print(limit_3())  # blocked
