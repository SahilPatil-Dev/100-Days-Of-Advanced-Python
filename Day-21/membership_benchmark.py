import time


def benchmark_membership():
    size = 200_000
    data_list = list(range(size))
    data_set = set(data_list)

    target = size - 1  # worst-case for list lookup

    # List membership
    start = time.perf_counter()
    target in data_list
    list_time = time.perf_counter() - start

    # Set membership
    start = time.perf_counter()
    target in data_set
    set_time = time.perf_counter() - start

    print(f"List membership time: {list_time:.8f} seconds")
    print(f"Set membership time:  {set_time:.8f} seconds")


if __name__ == "__main__":
    benchmark_membership()
