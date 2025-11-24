#!/usr/bin/env python3
"""1-concurrent_coroutines module
This module demonstrates running multiple asynchronous coroutines concurrently.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs multiple wait_random coroutines concurrently and returns
    the delays in ascending order of completion time.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for finished_coroutine in asyncio.as_completed(coroutines):
        delay = await finished_coroutine
        delays.append(delay)

    return delays
