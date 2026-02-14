import asyncio


counter = 0


async def increment_without_lock():
    global counter
    temp = counter
    await asyncio.sleep(0)
    counter = temp + 1


async def run_without_lock():
    global counter
    counter = 0
    tasks = [increment_without_lock() for _ in range(1000)]
    await asyncio.gather(*tasks)
    print("Counter without lock:", counter)


# ---- FIX WITH LOCK ----

lock = asyncio.Lock()


async def increment_with_lock():
    global counter
    async with lock:
        temp = counter
        await asyncio.sleep(0)
        counter = temp + 1


async def run_with_lock():
    global counter
    counter = 0
    tasks = [increment_with_lock() for _ in range(1000)]
    await asyncio.gather(*tasks)
    print("Counter with lock:", counter)


async def main():
    await run_without_lock()
    await run_with_lock()


if __name__ == "__main__":
    asyncio.run(main())
