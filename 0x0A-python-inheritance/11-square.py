#!/usr/bin/python3
"""
11-square module
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
