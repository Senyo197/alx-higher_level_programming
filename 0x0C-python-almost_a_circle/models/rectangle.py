#!/usr/bin/python3

from models.base import Base
"""A rectangle class"""


class Rectangle(Base):
    """The Rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new instance
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the rectangle
            y (int): The y-coordinate of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y is not an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle
        Returns:
            int: The area of the rctangle
        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using '#' and taking into account the x"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

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
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """A custom string representation of the rectangle
        Returns:
            Returns a string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"
