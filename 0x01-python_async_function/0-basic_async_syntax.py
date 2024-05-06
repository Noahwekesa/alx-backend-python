#!/usr/bin/env python3
"""
Async syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random delay between 0 and max_delay seconds
    (inclusive) and returns the delay.

    Args:
        max_delay: (defualt: 10)
    Returns:
        A float representing the random delay in seconds
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
