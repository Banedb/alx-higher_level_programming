#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """read_file function

    Reads a file and prints to stdout

    Args:
        filename (file): file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
