#!/usr/bin/python3
"""3-say_my_name
This module contains a single function for dividing all elements of a matrix
Functions:
    say_my_name(first_name, last_name=""): prints name with concat of given args
"""


def say_my_name(first_name, last_name=""):
    """Function to print name
    Purpose:
        print name from a concatenation of args
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
