#!/usr/bin/python3
"""Append to file module"""


def append_write(filename="", text=""):
    """Function to append text to file

    Args:
        filename (file): file to append to
        text (str): text to append

    Return:
        int: number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
        return count
