#!/usr/bin/python3
""" 100-append_after
    Module that executes a function to append a line
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    new = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            new += [line]
            if line.find(search_string) != -1:
                new += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(new))
