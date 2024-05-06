#!/usr/bin/env python3
"""
Tasks
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Takes an int and returns a asyncio.Task
    Args:
        max_delay: int
    Return:
        Task
    """

    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
