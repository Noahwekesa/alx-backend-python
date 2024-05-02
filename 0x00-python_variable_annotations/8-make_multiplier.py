#!/usr/bin/env python3
"""
module for Type Annotation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument
    And returns a function that multiplies a float by multiplier
    """

    def multiply(n: float) -> float:
        """
        Function that multiplies a float by multiplier
        """
        return n * multiplier

    return multiply
