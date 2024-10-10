#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats and returns their sum as a float.
    Args:
        mxd_lst: list[float | int]
    Return
        float: the sum of mxd_lst
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
