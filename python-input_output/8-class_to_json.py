#!/usr/bin/python3
""""Module with single function"""


def class_to_json(obj):
    """ function that returns the dictionary description"""
    return vars(obj)
