#!/usr/bin/python3
"""Module with recatangle class"""

from models.base import Base


class Rectangle(Base):
    """Class that describes a recatngle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes of a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangles using # shifted using x and y"""
        for spaces in range(self.__y):
            print()
        for spaces in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Updates and assigns argument to each attribute"""
        if args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

        else:
             try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.__width = kwargs['width']
            except KeyError:
                pass
            try:
                self.__height = kwargs['height']
            except KeyError:
                pass
            try:
                self.__x = kwargs['x']
            except KeyError:
                pass
            try:
                self.__y = kwargs['x']
            except KeyError:
                pass
