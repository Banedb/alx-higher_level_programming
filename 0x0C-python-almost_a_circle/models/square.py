#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inherits attributes from the super class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints instance information."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for width."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for width."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for count, value in enumerate(args[:4]):
                setattr(self, attrs[count], value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square instance"""
        attrs = ["id", "size", "x", "y"]
        return {f"{attr}": getattr(self, attr) for attr in attrs}
