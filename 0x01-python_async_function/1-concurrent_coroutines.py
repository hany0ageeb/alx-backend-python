#!/usr/bin/env python3
# 1-concurrent_coroutines.py
"""
Import wait_random from the previous python file that you’ve written and
write an async routine called wait_n that takes in 2 int arguments
(in this order):
n and max_delay.
You will spawn wait_random n times with the specified max_delay
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order
without using sort() because of concurrency.
"""
import asyncio
from typing import List, Callable


wait_random: Callable[[int], float] = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    Args:
        n: int number of spawned wait_random
        max_delay: int the specidfed max_delay for wait_random
    Return
        The list of all the delays (float values).
        The list of the delays should be in ascending order
        without using sort() because of concurrency.
    """
    result: List[float] =
    await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    result = sorted(result)
    return result
