#!/usr/bin/env python3
"""
measure_runtime should measure the total runtime and return it.
"""

measure_runtime = __import__("0-basic_cache").measure_runtime


async def main():
    """
    Main function
    """
    print(f"Total runtime: {await measure_runtime()}")
