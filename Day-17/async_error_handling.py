import asyncio


async def successful_task(name: str):
    await asyncio.sleep(1)
    print(f"{name} completed")
    return f"{name} result"


async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("Simulated API failure")


async def default_gather_behavior():
    print("\n--- Default gather behavior ---")
    try:
        await asyncio.gather(
            successful_task("Task A"),
            failing_task(),
            successful_task("Task C"),
        )
    except Exception as e:
        print(f"Gather raised exception: {e}")


async def controlled_gather_behavior():
    print("\n--- Controlled gather behavior (return_exceptions=True) ---")
    results = await asyncio.gather(
        successful_task("Task A"),
        failing_task(),
        successful_task("Task C"),
        return_exceptions=True,
    )

    print("Results:", results)


async def main():
    await default_gather_behavior()
    await controlled_gather_behavior()


if __name__ == "__main__":
    asyncio.run(main())
