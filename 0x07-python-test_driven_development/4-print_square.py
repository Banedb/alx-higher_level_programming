#!/usr/bin/python3
"""4-print_square
This module contains a single function to print squares
Functions:
    print_square(size): prints squares
"""


def print_square(size):
    """Function to print sqauares with #
    Purpose:
        print size-sized square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
