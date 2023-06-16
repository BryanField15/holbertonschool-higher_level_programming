#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """A class that define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        self.__width = width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        self.__height = height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
