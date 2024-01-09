#!/usr/bin/python3
"""Load, add, save"""


import sys


def las():
    """Takes arguments from the command line and adds them to a list
    then converts that list into json
    """
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"

    try:
        items = load(filename)
    except (FileNotFoundError, ValueError):
        items = []

    items.extend(sys.argv[1:])
    try:
        save(items, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


if __name__ == "__main__":
    las()
