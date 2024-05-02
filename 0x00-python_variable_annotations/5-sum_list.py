#!/usr/bin/env python3
"""
Module for Type Annotation
"""


def sum_list(input_list: list[float]) -> float:
    """
    Function that takes a list of integers as argument and returns their sum
    """
    total_sum = 0.0
    for num in input_list:
        total_sum += num
    return total_sum
