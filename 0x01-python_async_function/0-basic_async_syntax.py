#!/usr/bin/env python3
""" 0-basic_async_syntax.py """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ This function returns a  """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
