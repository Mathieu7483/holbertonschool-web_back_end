#!/usr/bin/env python3
"""7-to_kv module
This module contains a function that converts a float to a key-value pair.
"""
from typing import Tuple


def to_kv(k: float) -> Tuple[float, str]:
    """Converts a float number to a key-value pair.

    The key is the original float number, and the value is the string
    representation of the square of the float number.

    Args:
        k (float): The float number.

    Returns:
        Tuple[float, str]: A tuple containing the original float number
        and the string representation of its square.
    """
    return (k, str(k * k))
