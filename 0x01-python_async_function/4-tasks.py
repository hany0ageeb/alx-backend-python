#!/usr/bin/env python3
# 4-tasks.py
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
from typing import Callable, List
import asyncio

task_wait_random: Callable[[int], asyncio.Task] = __import__(
    '3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    code is nearly identical to wait_n except task_wait_random is being called
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for i in range(n)]
    result: List[float] = await asyncio.gather(*tasks)
    result = sorted(result)
    return result
