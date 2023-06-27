#!/usr/bin/python3
"""Module with recatangle class"""

from models.base import Base


class Rectangle(Base):
    """Class that describes a recatngle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes of a rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        self.__height = value

    @property
    def x(self):
        """Retrieve x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x value"""
        self.__x = value

    @property
    def y(self):
        """Retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y value"""
        self.__y = value
