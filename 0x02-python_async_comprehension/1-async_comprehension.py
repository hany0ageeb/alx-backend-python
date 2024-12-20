#!/usr/bin/env python3
# 1-async_comprehension.py
"""
Import async_generator from the previous task and then
write a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    collect 10 random numbers using an async comprehensing over async_generator
    Return
        the 10 random numbers
    """
    return [i async for i in async_generator()]
