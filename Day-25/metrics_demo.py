import inspect


def count_lines(func):
    return len(inspect.getsource(func).splitlines())


def messy():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    return a + b + c + d + e + f + g


def cleaner():
    values = [1, 2, 3, 4, 5, 6, 7]
    return sum(values)


if __name__ == "__main__":
    print("Messy lines:", count_lines(messy))
    print("Cleaner lines:", count_lines(cleaner))