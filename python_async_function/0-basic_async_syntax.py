#!/usr/bin/env python3
"""0-basic_async_syntax module
This module demonstrates the basic syntax of asynchronous functions in Python.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
