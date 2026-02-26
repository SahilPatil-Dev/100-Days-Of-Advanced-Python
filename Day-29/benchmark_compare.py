import time
import random


def list_membership(data, target):
    return target in data


def set_membership(data, target):
    return target in data


def benchmark():
    data = list(range(100000))
    data_set = set(data)

    target = random.choice(data)

    # Multiple runs
    runs = 1000

    start = time.perf_counter()
    for _ in range(runs):
        list_membership(data, target)
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(runs):
        set_membership(data_set, target)
    set_time = time.perf_counter() - start

    print(f"List membership time: {list_time:.6f}")
    print(f"Set membership time:  {set_time:.6f}")


if __name__ == "__main__":
    benchmark()
