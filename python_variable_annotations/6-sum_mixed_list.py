#!/usr/bin/env python3
"""6-sum_mixed_list module
This module contains a function that sums a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats and returns the result as a float.

    Args:
        input_list (List[Union[int, float]]): A list of integers
        and float numbers.
    Returns:
        float: The sum of all numbers in input_list.
    """
    return float(sum(input_list))
