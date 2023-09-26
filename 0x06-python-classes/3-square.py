#!/usr/bin/python3
"""A Square class"""


class Square:
    """Represents the Square"""

    def __init__(self, size=0):
        """Initialize the Square
        Arg:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Definition for area"""
        return self.__size * self.__size
