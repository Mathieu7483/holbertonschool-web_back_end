#!/usr/bin/env python3
"""0-add module
This module contains a function that adds two integers.
"""
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> float:
    """Adds two numbers and returns the result as a float.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.

    Returns:
        float: The sum of a and b.
    """
    return float(a + b)
