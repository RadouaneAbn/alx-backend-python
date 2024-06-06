#!/usr/bin/env python3
""" 7-to_kv.py """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple (k, v ** 2)

    Args:
        k (str): The string
        v (int or float): the number

    Returns: a tuple of teh string and the square of v
    """
    return (k, v * v)
