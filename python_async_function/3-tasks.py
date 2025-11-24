#!/usr/bin/env python3
"""3-tasks module
This module creates asynchronous tasks for multiple wait_random coroutines.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio Task that runs wait_random
    with the specified max_delay.
    Args:
        max_delay (int): Maximum delay value for wait_random.
    Returns:
        asyncio.Task: An asyncio Task running wait_random.
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)

    return task
