import time
import random


def find_duplicates_bruteforce(data):
    duplicates = set()
    n = len(data)

    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                duplicates.add(data[i])

    return duplicates


def find_duplicates_optimized(data):
    seen = set()
    duplicates = set()

    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


def benchmark():
    data = [random.randint(1, 5000) for _ in range(10000)]

    start = time.perf_counter()
    find_duplicates_bruteforce(data)
    brute_time = time.perf_counter() - start

    start = time.perf_counter()
    find_duplicates_optimized(data)
    opt_time = time.perf_counter() - start

    print(f"Bruteforce time: {brute_time:.6f}")
    print(f"Optimized time:  {opt_time:.6f}")


if __name__ == "__main__":
    benchmark()
