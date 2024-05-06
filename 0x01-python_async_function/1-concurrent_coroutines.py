#!/usr/bin/env python3
"""
module lets execute multiple coroutines at the same time
"""

import random
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay):
    """
    Takes n random delays concurently and returns them in ascending order.

    Args:
        n: no of random delays
        max_delay: upper random delay(default=10)
    Returns:
        list of floats representing the random delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = await asyncio.gather(*tasks)

    return delays
