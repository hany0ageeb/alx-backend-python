#!/usr/bin/env python3
"""
Write a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    function floor takes a float n as argument and returns the floor of the float.
    Args:
        n: float
    Return:
        int: the floor of n
    """
    return math.floor(n)
