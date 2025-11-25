#!/usr/bin/env python3
"""4-tasks module
This module creates multiple asyncio Tasks for wait_random coroutines.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs multiple task_wait_random tasks concurrently and returns
    the delays in ascending order of completion time.

    This function is nearly identical to wait_n (Tâche 1), but it calls
    task_wait_random (Tâche 3), which returns an already created Task object.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
