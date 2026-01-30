def request_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = request_counter()
print(counter())
print(counter())
print(counter())
