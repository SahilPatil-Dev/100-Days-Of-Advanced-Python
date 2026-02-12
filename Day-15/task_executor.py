import time
import threading
from multiprocessing import Process
from typing import List, Dict


def io_task(name: str) -> None:
    time.sleep(2)
    print(f"I/O task completed: {name}")


def cpu_task(name: str) -> None:
    # total = 0
    # for i in range(40_000_000):
    #     total += i
    sum(range(40_000_000))
    print(f"CPU task completed: {name}")


def execute_tasks(tasks: List[Dict[str, str]]) -> None:
    threads = []
    processes = []

    for task in tasks:
        if task["type"] == "io":
            t = threading.Thread(target=io_task, args=(task["name"],))
            threads.append(t)
            t.start()

        elif task["type"] == "cpu":
            p = Process(target=cpu_task, args=(task["name"],))
            processes.append(p)
            p.start()

    for t in threads:
        t.join()

    for p in processes:
        p.join()


if __name__ == "__main__":
    task_list = [
        {"type": "io", "name": "download"},
        {"type": "cpu", "name": "analysis"},
    ]

    start = time.time()
    execute_tasks(task_list)
    print(f"Total execution time: {time.time() - start:.2f} seconds")
