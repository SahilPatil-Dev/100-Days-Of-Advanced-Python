import time
from multiprocessing import Process


def cpu_task(name: str) -> None:
    print(f"Starting CPU task {name}")
    total = 0
    for i in range(50_000_000):
        total += i
    print(f"Finished CPU task {name}")


def run_sequential() -> None:
    start = time.time()

    cpu_task("A")
    cpu_task("B")

    end = time.time()
    print(f"Sequential CPU time: {end - start:.2f} seconds\n")


def run_parallel() -> None:
    start = time.time()

    p1 = Process(target=cpu_task, args=("A",))
    p2 = Process(target=cpu_task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"Parallel CPU time: {end - start:.2f} seconds\n")


if __name__ == "__main__":
    run_sequential()
    run_parallel()
