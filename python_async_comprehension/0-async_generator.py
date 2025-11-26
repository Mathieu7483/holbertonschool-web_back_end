#!/usr/bin/env python3
"""0-async_generator module
This module defines an asynchronous generator that yields
random numbers with a delay.
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yield 10 random float numbers between 0 and 10.

    This coroutine loops 10 times. On each iteration, it asynchronously waits
    for 1 second, generates a random float between 0 and 10, and yields it.

    Yields:
        float: A randomly generated float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = uniform(0, 10)
        yield random_number
