#!/usr/bin/python3
"""Module with class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that describes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Insitializes the attributes of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a formatted string"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        """Retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates and assigns argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.size = kwargs["size"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass
