#!/usr/bin/env python3
"""100-safe_first_element module
This module contains a function that safely retrieves the first element
of a list, returning None if the list is empty.
"""
from typing import List, Union, Optional


def safe_first_element(lst: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """Retrieves the first element of a list safely.

    If the list is empty, returns None. Otherwise, returns the first element,
    which can be an integer or a float.

    Args:
        lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        Optional[Union[int, float]]: The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    return None
