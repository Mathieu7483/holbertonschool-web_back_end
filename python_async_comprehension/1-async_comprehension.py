#!/usr/bin/env python3
"""1-async_comprehension module
This module defines an asynchronous function that
collects numbers from an asynchronous generator
using asynchronous comprehensions.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator
    using an asynchronous comprehension.

    This function calls the async_generator coroutine to get
    an asynchronous generator that yields random numbers.
    It then uses an asynchronous comprehension to collect
    10 numbers from the generator into a list.

    Returns:
        List[float]: A list of 10 randomly generated float numbers.
    """
    return [number async for number in async_generator()]
