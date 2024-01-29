#!/usr/bin/python3
"""7-add_item
    This script adds all arguments to a Python list and saves them to a file
"""


from sys import argv
from os.path import exists


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
f = "add_item.json"
if exists(f):
    my_list = load_from_json_file(f)
else:
    my_list = []
my_list.extend(argv[1:])
save_to_json_file(my_list, f)
