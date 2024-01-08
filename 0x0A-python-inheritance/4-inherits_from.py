#!/usr/bin/python3
"""Sub class module"""


def inherits_from(obj, a_class):
    """Determine if obj inherits from a_class (but isn't a direct instance)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
