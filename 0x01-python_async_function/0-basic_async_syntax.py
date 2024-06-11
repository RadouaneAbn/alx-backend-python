#!/usr/bin/env python3
""" 0-basic_async_syntax.py """
import random
from asyncio import sleep


async def wait_random(max_delay=10):
    """ This function returns a  """
    wait_time = random.uniform(0, max_delay)
    await sleep(wait_time)
    return wait_time
