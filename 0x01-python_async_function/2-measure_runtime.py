#!/usr/bin/env python3
"""
Module to measure execution time
"""

import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    returns the average time per call.

    Args:
        n: number of random delays to generate.
        max_delay:upper random delay (default: 10).

    Returns:
        A float representing the average execution time per call in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
