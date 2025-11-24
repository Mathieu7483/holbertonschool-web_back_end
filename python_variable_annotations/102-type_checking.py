#!/usr/bin/env python3
"""102-type_checking module
This module contains a function that zooms into a tuple by
repeating each element a specified number of times.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms into a tuple by repeating each element.

    Args:
        lst (Tuple): A tuple of elements to be zoomed.
        factor (int, optional): The number of times to repeat each element.
                                Defaults to 2.

    Returns:
        List: A new list with each element repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
