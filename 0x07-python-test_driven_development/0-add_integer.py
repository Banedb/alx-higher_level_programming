#!/usr/bin/python3
"""0-add_integer
This module contains a single function for performing addition operations
Functions:
    add_integer(a, b=98): Performs addition on two integers.
"""


def add_integer(a, b=98):
    """Addition function
    Returns: result of a + b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
