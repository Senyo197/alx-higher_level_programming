#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Checks whether or not object is subclass"""

    def area(self):
        """Area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer
        Args:
            name (str): The name of the value being validated
            value (int): The value to be validated
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the retangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Implement a square class"""
    def __init__(self, size):
        """Initialize a square
        Arg:
            size (int): Size of the new square
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
