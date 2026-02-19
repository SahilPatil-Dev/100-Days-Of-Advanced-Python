import time
import random

# Naive Version (Inefficient)
def count_actions_naive(logs):
    result = {}

    # Get unique users
    users = list(set(user for user, _ in logs))
    
    # For each user, scan entire logs again
    for user in users:
        user_actions = {}

        for log_user, action in logs:
            if log_user == user:
                user_actions[action] = user_actions.get(action, 0) + 1

        result[user] = user_actions

    return result


# Optimized Version (Single Pass)
def count_actions_optimized(logs):
    result = {}

    for user, action in logs:
        if user not in result:
            result[user] = {}

        result[user][action] = result[user].get(action, 0) + 1

    return result



# Benchmark Function

def benchmark():
    users = [f"user_{i}" for i in range(1000)]
    actions = ["login", "logout", "purchase", "view"]

    # Generate random logs
    logs = [
        (random.choice(users), random.choice(actions))
        for _ in range(20000)
    ]

    # Benchmark naive version
    start = time.perf_counter()
    naive_result = count_actions_naive(logs)
    naive_time = time.perf_counter() - start

    # Benchmark optimized version
    start = time.perf_counter()
    optimized_result = count_actions_optimized(logs)
    optimized_time = time.perf_counter() - start

    print(f"Naive time:      {naive_time:.6f} seconds")
    print(f"Optimized time:  {optimized_time:.6f} seconds")

    # Optional correctness check
    print("\nResults are identical:", naive_result == optimized_result)



# Run the benchmark

if __name__ == "__main__":
    benchmark()
