#!/usr/bin/env python3
"""
modeule for Type Annotation
"""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Function that takes a list of strings as argument
    And returns a list of integers representing the lengths of the strings
    """
    return [(i, len(i)) for i in lst]
