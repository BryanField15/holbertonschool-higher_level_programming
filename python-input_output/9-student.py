#!/usr/bin/python3
""""Class Student that describes a student"""


class Student:
    """Simple attempt to model a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student attibutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
