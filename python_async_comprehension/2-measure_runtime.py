#!/usr/bin/env python3
"""2-measure_runtime module
This module measures the total runtime of multiple asynchronous coroutines.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of executing
    async_comprehension four times in parallel.

    This coroutine executes async_comprehension four times concurrently using
    asyncio.gather and measures the total time taken.

    Returns:
        float: The total time taken to execute all four instances, in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
