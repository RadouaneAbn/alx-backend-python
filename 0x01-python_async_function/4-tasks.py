#!/usr/bin/env python3
""" 4-tasks.py """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int):
    async def wait_n(n: int, max_delay: int) -> List[float]:
        """ This function return a task that exexute wait_random for n times
            and append the wait time to a list when it finishes
            executing each time
        """
        tasks = [wait_random(max_delay) for _ in range(n)]
        delays = []
        for task in asyncio.as_completed(tasks):
            delays.append(await task)
        return delays
    return await asyncio.create_task(wait_n(n, max_delay))
