#!/usr/bin/python3
"""Test if it is a kind of class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance ofa given class.

    Args:
        obj: The object to check.
        a_class: The class to match the type or inheritance against.

    Returns:
        bool: True otherwise False.
    """
    return isinstance(obj, a_class)
