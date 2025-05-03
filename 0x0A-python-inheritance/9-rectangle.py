#!/usr/bin/python3
"""Base Geometry module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
