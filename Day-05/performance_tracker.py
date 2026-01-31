import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")

        return result

    return wrapper


@measure_time
def slow_function():
    time.sleep(2)
    return "Done"


# Example run
print(slow_function())
