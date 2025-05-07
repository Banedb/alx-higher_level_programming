#!/usr/bin/python3
"""base module"""

import json
import csv
import turtle
import itertools


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws class instances using turtle"""
        turtle.bgcolor("grey")
        t = turtle.Turtle()
        t.pensize(5)
        t.hideturtle()
        for rect, sq in itertools.zip_longest(list_rectangles, list_squares):
            if rect:
                t.penup()
                t.goto(rect.x, rect.y)
                t.pendown()
                t.pencolor("black")
                for _ in range(2):
                    t.forward(rect.width)
                    t.right(90)
                    t.forward(rect.height)
                    t.right(90)
            if sq:
                t.penup()
                t.goto(sq.x, sq.y)
                t.pendown()
                t.pencolor("white")
                for _ in range(4):
                    t.forward(sq.size)
                    t.right(90)
        turtle.done()

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries
        (list_dictionaries)."""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        """Loads and returns a list from the JSON string representation
        (json_string)."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects
        (list_objs) to a file."""
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            dict_list = ([obj.to_dictionary() for obj in list_objs]
                         if list_objs else [])
            f.write(cls.to_json_string(dict_list))
            # json.dump(dict_list, f)

    @classmethod
    def load_from_file(cls):
        """Returns a list of objects created from a list of dict loaded from
        json string in file '<class_name>.json'."""
        try:
            with open(f"{cls.__name__}.json", encoding="utf-8") as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**dict_i) for dict_i in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance of cls with dictionary attributes"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv string representation of a list of objects
        (list_objs) to a file."""
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            if not list_objs:
                return
            dict_list = [obj.to_dictionary() for obj in list_objs]
            writer = csv.DictWriter(f, fieldnames=list(dict_list[0].keys()))
            writer.writeheader()
            writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Writes the JSON string representation of a list of objects
        (list_objs) to a file."""
        try:
            with open(f"{cls.__name__}.csv", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                # print(list(reader))
                dict_list = [{k: int(v) for k, v in dict_i.items()}
                             for dict_i in list(reader)]
                return [cls.create(**dict_i) for dict_i in dict_list]
        except FileNotFoundError:
            return []
