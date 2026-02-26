import cProfile
import pstats
import io


def slow_duplicate_counter(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                count += 1
    return count


def optimized_duplicate_counter(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return len(duplicates)


if __name__ == "__main__":
    data = list(range(5000)) + list(range(2500))

    print("Profiling slow version...\n")
    profiler = cProfile.Profile()
    profiler.enable()
    slow_duplicate_counter(data)
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumtime")
    stats.print_stats(10)
    print(stream.getvalue())

    print("Profiling optimized version...\n")
    profiler = cProfile.Profile()
    profiler.enable()
    optimized_duplicate_counter(data)
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumtime")
    stats.print_stats(10)
    print(stream.getvalue())
