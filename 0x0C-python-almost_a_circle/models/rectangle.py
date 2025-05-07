#!/usr/bin/python3
"""rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Inherits from class Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises an instance of Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Prints instance information."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints a Rectangle instance with '#'."""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes."""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for count, value in enumerate(args[:5]):
                setattr(self, attrs[count], value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance"""
        attrs = ["id", "width", "height", "x", "y"]
        return {f"{attr}": getattr(self, attr) for attr in attrs}
