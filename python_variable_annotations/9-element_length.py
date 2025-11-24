#!/usr/bin/env python3
"""9-element_length module
This module contains a function that returns the length of a given list.
"""
from typing import List


def element_length(lst: List[any]) -> int:
    """Returns the length of the given list.

    Args:
        lst (List[any]): The list whose length is to be calculated.

    Returns:
        int: The length of the list.
    """
    return len(lst)
