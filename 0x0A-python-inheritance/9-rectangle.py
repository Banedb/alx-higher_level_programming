#!/usr/bin/python3
"""Base Geometry module"""


class BaseGeometry:
    """Class with unimplemented area and integer validation"""

    def area(self):
        """Raise an Exception for unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.
        Raises TypeError or ValueError with appropriate messages.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry, adds width and height validation"""

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height after validation.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry, with area and printing."""

    def __init__(self, width, height):
        """
        Initialize Rectangle with private width and height after validation.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implements area calculation for the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Provides the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
