#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes each object
        args:
            size (int): size of the square
            position (tuple): position of num in square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """"getter method
        Return:
        size as RO
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets square to position
        args:
            value (tuple): pos in the square
        """
        if (not isinstance(value, tuple)) or (len(value) != 2) or \
           (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for _ in (range(self.__position[1])):
                print()
            for _ in (range(self.__size)):
                print(" " * self.__position[0] + "#" * self.__size)
