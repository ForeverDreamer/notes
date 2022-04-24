import asyncio


# Coroutines
async def nested():
    return 42


async def main0():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    await nested(await nested())  # will print "42".


# Tasks
async def main1():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)


# Futures
# async def main2():
#     await function_that_returns_a_future_object()
#
#     # this is also valid:
#     await asyncio.gather(
#         function_that_returns_a_future_object(),
#         some_python_coroutine()
#     )

if __name__ == "__main__":
    asyncio.run(main1())
