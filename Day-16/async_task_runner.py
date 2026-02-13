import asyncio
import time
from datetime import datetime


async def simulated_request(name: str) -> str:
    print(f"{datetime.now()} - Sending request: {name}")
    await asyncio.sleep(2)
    print(f"{datetime.now()} - Completed request: {name}")
    return f"{name} done"


async def run_tasks():
    start = time.time()

    results = await asyncio.gather(
        simulated_request("User API"),
        simulated_request("Payment API"),
        simulated_request("Notification API"),
    )

    print(f"\nResults: {results}")
    print(f"Total execution time: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(run_tasks())
