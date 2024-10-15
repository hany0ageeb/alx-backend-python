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


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
