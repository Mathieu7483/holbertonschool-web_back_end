#!/usr/bin/env python3
"""1-concurrent_coroutines module
This module demonstrates running multiple asynchronous coroutines concurrently.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs multiple wait_random coroutines concurrently.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)


    sorted_delays = []
    delays_copy = list(delays)

    while delays_copy:
        min_delay = min(delays_copy)
        sorted_delays.append(min_delay)
        delays_copy.remove

    return sorted_delays
