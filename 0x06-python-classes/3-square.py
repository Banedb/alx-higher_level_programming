#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """A class Square that defines a square
    Atributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """initializes each object
        args:
            __size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """finds square area from size
        return:
            the square area
        """
        return self.__size ** 2
