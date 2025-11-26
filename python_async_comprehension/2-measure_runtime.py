#!/usr/bin/env python3
"""2-measure_runtime module
This module measures the total runtime of multiple asynchronous coroutines.
"""
import asyncio
import time
from typing import Callable


async def measure_runtime(coro: Callable, n: int) -> float:
    """Measures the total runtime of executing a coroutine n times concurrently.

    This function creates n tasks for the given coroutine and runs them
    concurrently using asyncio.gather. It measures the time taken to complete
    all tasks and returns the total runtime.

    Args:
        coro (Callable): The asynchronous coroutine function to be executed.
        n (int): The number of times to execute the coroutine.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(coro() for _ in range(n)))
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
