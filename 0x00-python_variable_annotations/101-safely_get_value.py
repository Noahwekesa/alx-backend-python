#!/usr/bin/env python3
"""
Module return values, add type annotations to the function
"""

from typing import Any, Union


def safely_get_value(
    dct: dict, key: Any, default: Union[Any, None] = None
) -> Union[Any, None]:
    if key in dct:
        return dct[key]
    else:
        return default
