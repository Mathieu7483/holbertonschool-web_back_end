#!/usr/bin/env python3
"""7-to_kv module
This module contains a function that converts a string and a number
(int or float) to a tuple containing the string and the square of the number
annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key (string) and a value (int or float)
    into a key-value pair.

    The key is the original string, and the value is the square of the
    number, annotated as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The numeric value (int or float).

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square
        of v, cast to a float.
    """
    return (k, float(v * v))
