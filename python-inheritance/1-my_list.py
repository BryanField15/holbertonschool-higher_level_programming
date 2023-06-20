#!/usr/bin/python3
"""Module for MyList subclass"""


class MyList(list):
    """Class that inherits class list"""
    def print_sorted(self):
        """Method prints the list, sorted ascedning"""
        print(sorted(self))

    def __str__(self):
        return super().__str__()
