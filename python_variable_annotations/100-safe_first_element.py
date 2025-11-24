#!/usr/bin/env python3
"""100-safe_first_element module
This module contains a function that safely retrieves the first element
of a list, returning None if the list is empty.
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Retrieves the first element of a sequence safely.

    If the sequence is empty, returns None. Otherwise,
    returns the first element,
    whose type is inferred from the sequence.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple, string)
        of any type.

    Returns:
        Optional[Any]: The first element of the sequence if it exists,
        otherwise None. The type of the return value is inferred from the
        sequence elements.
    """
    if lst:
        return lst[0]
    return None
