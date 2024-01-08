#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class

    Inherits from the list class
    """
    def print_sorted(self):
        """print the list in ascending order"""
        print(sorted(self))
