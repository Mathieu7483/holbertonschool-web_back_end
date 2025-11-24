#!/usr/bin/env python3
"""101-safely_get_value module
This module contains a function that safely retrieves a value from a
dictionary given a key, returning a default value (None by default)
if the key does not exist.
"""
from typing import Mapping, Optional, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
                     key: Any,
                     default: Optional[T] = None) -> Union[T, Optional[T]]:
    """Safely retrieves a value from a dictionary by key.

    If the key exists in the dictionary,
    returns the corresponding value (type T).
    If the key does not exist,
    returns the provided default value (type Optional[T]).

    Args:
        dct (Mapping): A dictionary-like object (Mapping[Any, T]).
        key (Any): The key to look for in the dictionary (Any type).
        default (Optional[T], optional):
        The value to return if the key is not found.
        Defaults to None.

    Returns:
        Optional[T]: The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    return default
