#!/usr/bin/python3
"""A Square class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the square.
        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the square.
        Args:
            value (int): The new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)
