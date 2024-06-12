#!/usr/bin/env python3
""" 2-measure_runtime.py """

import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        This function returns the time needed to execute all tasks
        in parallel.
    """
    tasks = [async_comprehension()] * 4
    start = time()
    await asyncio.gather(*tasks)
    return time() - start
