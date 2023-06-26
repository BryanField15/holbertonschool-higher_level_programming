#!/usr/bin/python3
"""Module with class Base"""


class Base:
    """Class that manages id attribute of future classes"""
    __nb_objects = 0 #private class attribute

    def __init__(self, id=None):
        """Initialize class attibutes"""
        if id is not None:
           self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
