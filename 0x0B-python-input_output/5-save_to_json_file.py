#!/usr/bin/python3
"""Save Object to a file

Writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """save to json file

    Args:
        my_obj: object to convert to json
        filename: file to save it to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
