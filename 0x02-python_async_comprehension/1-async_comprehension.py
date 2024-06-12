#!/usr/bin/env python3
""" async_comprehension """

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
        This funtion returns a list of the 10 random numbers
        returned by async_generator.
    """
    return [n async for n in async_generator()]
