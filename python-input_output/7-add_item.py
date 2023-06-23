#!/usr/bin/python3
"""script that adds arguments to a Python list and saves them to a file"""


import json
import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""script that adds arguments to a Python list and saves them to a file"""
filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

args = sys.argv[1:]
my_list.extend(args)
save_to_json_file(my_list, filename)
