#!/usr/bin/env python3
"""
modeule for Type Annotation
"""

from typing import List


def element_length(lst: List[str]) -> List[int]:
    """
    Function that takes a list of strings as argument
    And returns a list of integers representing the lengths of the strings
    """
    return [len(i) for i in lst]
