import asyncio
import time


async def fake_api_call(name: str) -> str:
    print(f"Starting API call: {name}")
    await asyncio.sleep(2)
    print(f"Finished API call: {name}")
    return f"Response from {name}"


async def run_sequential():
    start = time.time()

    await fake_api_call("A")
    await fake_api_call("B")

    print(f"Sequential async time: {time.time() - start:.2f} seconds\n")


async def run_concurrent():
    start = time.time()

    await asyncio.gather(
        fake_api_call("A"),
        fake_api_call("B"),
    )

    print(f"Concurrent async time: {time.time() - start:.2f} seconds\n")


if __name__ == "__main__":
    asyncio.run(run_sequential())
    asyncio.run(run_concurrent())
