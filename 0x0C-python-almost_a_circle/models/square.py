#!/usr/bin/python3

from models.rectangle import Rectangle
"""A rectangle class"""


class Square(Rectangle):
    """The Rectangle class that inherits from the Base class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a new instance
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the rectangle
            y (int): The y-coordinate of the rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments in the order of id, width, height, x and y
        Args:
            A sequence of values to update the attributes in the order
             specified
        Kwargs:
            Keyworded argument that represents attribute and their names
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
