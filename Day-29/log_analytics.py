import random
import time
import cProfile
import pstats
import io


def generate_logs(n=100000):
    users = [f"user_{i}" for i in range(1000)]
    actions = ["login", "logout", "purchase"]
    return [(random.choice(users), random.choice(actions)) for _ in range(n)]


def naive_count(logs):
    result = {}
    for user, action in logs:
        if user not in result:
            result[user] = {}
        if action not in result[user]:
            result[user][action] = 0
        result[user][action] += 1
    return result


def optimized_count(logs):
    from collections import defaultdict

    result = defaultdict(lambda: defaultdict(int))
    for user, action in logs:
        result[user][action] += 1
    return result


if __name__ == "__main__":
    logs = generate_logs()

    print("Profiling naive version...\n")
    profiler = cProfile.Profile()
    profiler.enable()
    naive_count(logs)
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumtime")
    stats.print_stats(10)
    print(stream.getvalue())

    print("Profiling optimized version...\n")
    profiler = cProfile.Profile()
    profiler.enable()
    optimized_count(logs)
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumtime")
    stats.print_stats(10)
    print(stream.getvalue())
