#!/usr/bin/python3
"""Module with class Base"""

import json


class Base:
    """Class that manages id attribute of future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class attibutes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is  None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
