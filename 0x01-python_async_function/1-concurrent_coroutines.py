#!/usr/bin/env python3
""" 1-concurrent_coroutines.py """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ This function execute wait_random for n times
        and append the wait time to a list when it finishes
        executing each time
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
