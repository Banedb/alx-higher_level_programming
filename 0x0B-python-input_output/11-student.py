#!/usr/bin/python3
"""Module that defines the class Student."""


class Student:
    """Class to create student instances."""

    def __init__(self, first_name, last_name, age):
        """Initialises an instance of Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
