import asyncio


async def long_running_task():
    try:
        while True:
            print("Task running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled. Cleaning up...")
        await asyncio.sleep(0.5)
        print("Cleanup complete.")
        raise


async def main():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(3)

    print("Cancelling task...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task fully cancelled.")


if __name__ == "__main__":
    asyncio.run(main())
