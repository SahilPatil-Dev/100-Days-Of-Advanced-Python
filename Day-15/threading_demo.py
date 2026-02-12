import time
import threading


def io_task(name: str) -> None:
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Finished task {name}")


def run_sequential() -> None:
    start = time.time()

    io_task("A")
    io_task("B")

    end = time.time()
    print(f"Sequential time: {end - start:.2f} seconds\n")


def run_threaded() -> None:
    start = time.time()

    t1 = threading.Thread(target=io_task, args=("A",))
    t2 = threading.Thread(target=io_task, args=("B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"Threaded time: {end - start:.2f} seconds\n")


if __name__ == "__main__":
    run_sequential()
    run_threaded()
