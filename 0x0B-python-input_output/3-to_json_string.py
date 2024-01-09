#!/usr/bin/python3
"""Object to Json Module

Uses json dump to encode object
"""


import json


def to_json_string(my_obj):
    """Converts object to json sting

    Args:
        my_object (py object): object to convert

    Return:
        json
    """
    return json.dumps(my_obj)
