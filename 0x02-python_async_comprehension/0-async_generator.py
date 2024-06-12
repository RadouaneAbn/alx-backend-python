#!/usr/bin/env python3
"""0-async_generator.py  """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        This funtion loops 10 times, wait 1 second then yield a random number
        between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
    
