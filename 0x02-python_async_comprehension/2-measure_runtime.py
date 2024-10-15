#!/usr/bin/env python3
# 2-measure_runtime.py
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    measure the total runtime and return it
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    return time.time() - start
