#!/usr/bin/env python3
"""
module for Type Annotation
"""


def make_multiplier(multiplier: float) -> callable:
    """
    Function that takes a float multiplier as argument
    And returns a function that multiplies a float by multiplier
    """

    def func(n: float) -> float:
        return n * multiplier

    return func
