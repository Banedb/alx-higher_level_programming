#!/usr/bin/python3
"""101-add_attribute module"""


def can_assign_attr(obj, attr):
    """Checks if obj can be assigned an attribute."""
    if not hasattr(obj, "__dict__"):
        return False

    cls = type(obj)
    slots = getattr(cls, "__slots__", None)

    if not slots:  # Any attribute can be set
        return True

    if isinstance(slots, str):  # Check if slots is str
        return slots == attr

    return attr in slots  # check if attr is in slots list/tuple


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible."""
    if can_assign_attr(obj, value):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
