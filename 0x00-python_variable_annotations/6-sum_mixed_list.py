#!/usr/bin/env python3
""" 6-sum_mixed_list.py """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the numbers in the list.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers or floats

    Returns: the sum of all numbers in the list
    """
    return sum(mxd_lst)
