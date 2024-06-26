#!/usr/bin/env python3
"""
Type-annotated function safe_first_element
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that returns the first element of a list
    """
    if lst:
        return lst[0]
    else:
        return None
