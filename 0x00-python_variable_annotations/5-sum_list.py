#!/usr/bin/env python3
"""
Module for Type Annotation
"""

type Input_list = List[float]


def sum_list(input_list: Input_list) -> float:
    """
    Function that takes a list of integers as argument and returns their sum
    """
    return sum(input_list)
