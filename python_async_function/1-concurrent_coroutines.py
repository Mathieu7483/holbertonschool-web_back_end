#!/usr/bin/env python3
"""1-concurrent_coroutines module
This module demonstrates running multiple asynchronous coroutines concurrently.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n():
    """Runs multiple wait_random coroutines concurrently.

    Returns:
        List[float]: A list of delay times from each coroutine.
    """
    tasks = [wait_random() for _ in range(5)]
    delays = await asyncio.gather(*tasks)
    return delays
