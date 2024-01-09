#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """Reads a file, converts content to json

    Arg:
        filename (file): file to read from
    Return:
        json representation of object read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
