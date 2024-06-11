#!/usr/bin/env python3
""" 0-basic_async_syntax.py """
from typing import Union
import random
from asyncio import sleep


async def wait_random(max_delay: Union[int, float]=10) -> float:
    """ This function returns a  """
    wait_time = random.uniform(0, max_delay)
    await sleep(wait_time)
    return wait_time
