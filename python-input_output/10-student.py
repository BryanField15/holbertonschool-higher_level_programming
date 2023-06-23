#!/usr/bin/python3
""""Class Student that describes a student"""


class Student:
    """Simple attempt to model a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student attibutes
        :param first_name: The student's first name
        :param last_name: The student's last name
        :param age: The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
