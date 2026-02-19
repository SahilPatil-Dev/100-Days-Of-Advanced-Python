import time
import random


# O(n²) Version
def find_pair_bruteforce(transactions, target):
    n = len(transactions)

    for i in range(n):
        for j in range(i + 1, n):
            if transactions[i] + transactions[j] == target:
                return (transactions[i], transactions[j])

    return None


# O(n) Version Using Dictionary
def find_pair_optimized(transactions, target):
    seen = {}

    for amount in transactions:
        complement = target - amount

        if complement in seen:
            return (complement, amount)

        seen[amount] = True

    return None


def benchmark():
    # Generate random transactions
    size = 50000
    transactions = [random.randint(1, 5000) for _ in range(size)]

    # Ensure at least one valid pair exists
    transactions[-2] = 1234
    transactions[-1] = 4321
    target = 1234 + 4321

    print(f"Dataset size: {size}")
    print(f"Target: {target}")
    print("-" * 40)

    # Benchmark brute force
    start = time.perf_counter()
    result_brute = find_pair_bruteforce(transactions, target)
    brute_time = time.perf_counter() - start

    print("Bruteforce Result:", result_brute)
    print(f"Bruteforce Time: {brute_time:.6f} seconds")

    print("-" * 40)

    # Benchmark optimized
    start = time.perf_counter()
    result_opt = find_pair_optimized(transactions, target)
    opt_time = time.perf_counter() - start

    print("Optimized Result:", result_opt)
    print(f"Optimized Time: {opt_time:.6f} seconds")

    print("-" * 40)

    print(f"Speed difference: {brute_time / opt_time:.2f}x faster")


if __name__ == "__main__":
    benchmark()
