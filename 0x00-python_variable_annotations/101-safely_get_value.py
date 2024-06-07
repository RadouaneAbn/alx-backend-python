#!/usr/bin/env python3
""" 101-safely_get_value.py """
from typing import Union, Any, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """ This function return the value of a key in a dict """
    if key in dct:
        return dct[key]
    else:
        return default
