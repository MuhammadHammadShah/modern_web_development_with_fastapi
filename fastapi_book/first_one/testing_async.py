import asyncio
import time


def q():
    print("Why can't")
    time.sleep(4)


def a():
    print("timing")


def main():
    q()
    a()


main()


async def async_q():
    print("why can't i do it")
    await asyncio.sleep(4)


async def async_a():
    print("timing is good")


async def async_main():
    await asyncio.gather(async_q(), async_a())


asyncio.run(async_main())

