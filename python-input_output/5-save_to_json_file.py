#!/usr/bin/python3
"""Moduel with one function"""


import json


def save_to_json_file(my_obj, filename):
    """Function writes an Object to text file, using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
