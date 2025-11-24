#!/usr/bin/env python3
"""5-sum_list module
This module contains a function that sums a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats and returns the result as a float.

    Args:
        input_list (List[float]): A list of float numbers.
    Returns:
        float: The sum of all float numbers in input_list.
    """
    return sum(input_list)
