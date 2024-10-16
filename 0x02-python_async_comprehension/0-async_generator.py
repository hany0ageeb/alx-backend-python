#!/usr/bin/env python3
# 0-async_generator.py
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    i = 0
    while i < 10:
        yield random.random() * 10
        await asyncio.sleep(1)
        i += 1
