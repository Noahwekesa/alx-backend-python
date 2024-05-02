#!/usr/bin/env python3
"""
Module for Type Annotation
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers as argument and returns their sum
    """
    return sum(mxd_lst)
