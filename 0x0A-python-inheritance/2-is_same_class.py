#!/usr/bin/python3
"""Same class module

Checks if an object belongs to the same class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
