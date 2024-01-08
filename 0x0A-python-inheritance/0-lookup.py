#!/usr/bin/python3
"""Lookup Module

Returns a list of available attributes and methods of an object
"""


def lookup(obj):
    """lookup function

    Arg:
        obj (object): the object to list its attributes

    Returns:
        list of attributes and methods
    """
    return dir(obj)
