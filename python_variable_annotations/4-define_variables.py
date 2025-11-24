#!/usr/bin/env python3
"""4-define_variables module
This module defines variables with specific types using variable annotations.
"""
import math


a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"


def annotated_function(
        a: int,
        pi: float,
        i_understand_annotations: bool,
        school: str
) -> str:
    """Example function with variable annotations.

    Args:
        a (int): An integer parameter.
        pi (float): A float parameter.
        i_understand_annotations (bool): A boolean parameter.
        school (str): A string parameter.

    Returns:
        str: A string representation of the parameters.
    """
    return f"a: {a}, b: {pi}, c: {i_understand_annotations}, d: {school}"
