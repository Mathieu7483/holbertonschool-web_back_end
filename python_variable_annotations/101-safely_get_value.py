#!/usr/bin/env python3
"""101-safely_get_value module
This module contains a function that safely retrieves a value from a
dictionary given a key, returning a default value (None by default)
if the key does not exist.
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
                     key: Any,
                     default: Union[T] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary by key.

    Args:
        dct (Mapping[Any, T]): A dictionary-like object.
        key (Any): The key to look for.
        default (Optional[T], optional):
        The value to return if the key is not found.

    Returns:
        Union[T, Optional[T]]: The value (type T) or the default (Optional[T]).
    """
    if key in dct:
        return dct[key]
    return default
