#!/usr/bin/env python3
"""8-make_multiplier module
This module contains a function that creates a multiplier function
based on a given float factor.
"""
from typing import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    """Creates a multiplier function that
    multiplies its input by the given factor.

    Args:
        factor (float): The factor by which to multiply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the factor.
    """
    def multiplier(number: float) -> float:
        """Multiplies the input number by the predefined factor.

        Args:
            number (float): The number to be multiplied.

        Returns:
            float: The result of multiplying number by factor.
        """
        return number * multiplier

    return multiplier
