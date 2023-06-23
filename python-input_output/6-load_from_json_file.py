#!/usr/bin/python3
"""Moduel with one function"""


import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        data = json.load(f)
        return data
