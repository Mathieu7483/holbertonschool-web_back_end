#!/usr/bin/env python3
"""101-safely_get_value module
This module contains a function that safely retrieves a value from a
dictionary given a key, returning None if the key does not exist.
"""
from typing import Mapping, Optional, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[str, T], key: str) -> Optional[T]:
    """Safely retrieves a value from a dictionary by key.

    If the key exists in the dictionary, returns the corresponding value.
    If the key does not exist, returns None.

    Args:
        dct (Mapping[str, T]): A dictionary with string keys and values of
        any type.
        key (str): The key to look for in the dictionary.
    Returns:
        Optional[T]: The value associated with the key if it exists,
        otherwise None. The type of the return value is inferred from
        the dictionary values.
    """
    return dct.get(key, None)
