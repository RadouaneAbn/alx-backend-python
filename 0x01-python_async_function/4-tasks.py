#!/usr/bin/env python3
""" 4-tasks.py """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This function execute task_wait_random for n times
        and append the wait time to a list when it finishes
        executing each time
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
