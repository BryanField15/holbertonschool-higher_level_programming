#!/usr/bin/python3
"""Module with class rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle"""
    def __init__(self, width, height):
        """Initialize the recangles dimensions"""
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
