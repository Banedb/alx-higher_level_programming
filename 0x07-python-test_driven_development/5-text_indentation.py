#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' or ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    skip = True
    for char in text:
        if char == ' ' and skip:
            continue
        print(char, end='')
        skip = False
        if char == '\n':
            skip = True
        if char in ('.', '?', ':'):
            print("\n")
            skip = True
