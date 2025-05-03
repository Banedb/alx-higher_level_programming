#!/usr/bin/python3
"""
100-my_int module
"""


class MyInt(int):
    """Reverse implementation of != and == operators"""
    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
