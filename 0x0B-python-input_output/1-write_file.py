#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """write_file

    writes to a file

    Args:
        filename (file): file object to write to
        text (str): test to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        chars = f.write(text)
        return chars
