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
