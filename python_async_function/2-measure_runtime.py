#!/usr/bin/env python3
"""2-measure_runtime module
This module measures the total runtime of multiple asynchronous coroutines.
"""
import asyncio
import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(
    n: int, max_delay: int, wait_n_func: Callable[[int, int], asyncio.Future]
) -> float:
    """Measures the total runtime of running wait_n coroutines.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.
        wait_n_func (Callable[[int, int], asyncio.Future]):
        The wait_n function to run.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n_func(n, max_delay))
    end_time = time.time()
    return end_time - start_time
