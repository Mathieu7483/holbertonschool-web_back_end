#!/usr/bin/env python3
"""0-async_generator module
This module defines an asynchronous generator that yields
random numbers with a delay.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields 10 random numbers
    between 0 and 10, each after a random delay between 0 and 10 seconds.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random(0, 10)
        yield random_number
