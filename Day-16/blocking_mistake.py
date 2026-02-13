import asyncio
import time


async def bad_async_task(name: str):
    print(f"Starting task: {name}")
    time.sleep(2)  # ❌ Blocking call
    print(f"Finished task: {name}")


async def main():
    start = time.time()

    await asyncio.gather(
        bad_async_task("A"),
        bad_async_task("B"),
    )

    print(f"Total time: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
