#!/usr/bin/env python3
"""9-element_length module
This module contains a function that calculates the length of each element
in an iterable of sequences and returns a list of (element, length) tuples.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the length of each sequence element in the iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence objects
                                  (e.g., list of strings, list of lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains the original element and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
