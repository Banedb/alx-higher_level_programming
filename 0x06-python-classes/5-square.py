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
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """"getter method
        Return:
        size as RO
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets value of size
        args:
            value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finds square area from size
        return:
            the square area
        """
        return self.__size ** 2

    def my_print(self):
        """print the square as #"""
        if not self.__size:
            print()
        else:
            for _ in (range(self.__size)):
                print("#" * self.__size)
