#!/usr/bin/env python3
""" 9-element_length.py """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Creates a list of all elements in the Iterable with its length

    Args:
        lst (iterable): The list of elements

    Returns: a list of tuple (item, item_length)
    """
    return [(i, len(i)) for i in lst]
