#!/usr/bin/env python3
""" 8-make_multiplier.py """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    makes a funtion that calculates the multiplication of
    multiplier and a float

    Args:
        multiplier (float): The multiplier

    Returns: a function that calculates the multiplication of
        multiplier and a float
    """
    def multiply(n: float) -> float:
        """
        Calculates the multiplication of multiplier and a float

        Args:
            n (float): The given float

        Returns: The result of teh multiplication
        """
        return n * multiplier
    return multiply
