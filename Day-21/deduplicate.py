import time
import random


def deduplicate_naive(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def deduplicate_optimized(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def benchmark(size):
    items = [random.randint(0, size // 2) for _ in range(size)]

    # Measure naive
    start = time.perf_counter()
    deduplicate_naive(items)
    naive_time = time.perf_counter() - start

    # Measure optimized
    start = time.perf_counter()
    deduplicate_optimized(items)
    optimized_time = time.perf_counter() - start

    print(f"Size: {size}")
    print(f"Naive time:      {naive_time:.6f} sec")
    print(f"Optimized time:  {optimized_time:.6f} sec")
    print("-" * 40)


if __name__ == "__main__":
    for size in [1000, 5000, 10000, 20000]:
        benchmark(size)
