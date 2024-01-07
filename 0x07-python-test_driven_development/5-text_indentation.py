#!/usr/bin/python3
"""5-text_indentation
This module contains a single function to print squares
Functions:
    text_indentation(text): prints squares
"""


def text_indentation(text):
    """Function to print sqauares with #
    Purpose:
        print size-sized square with #
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip = False
    new_text = ""
    for char in text:
        if (skip and char == ' '):
            continue
        if skip and char != ' ' and char != '\n':
            skip = False
        if char in '?.:':
            new_text += char + "\n"
            print(new_text.strip(" "))
            skip = True
            new_text = ""
        else:
            new_text += char
            if char == '\n':
                skip = True
    print(new_text.strip(" "), end="")
