#!/usr/bin/python3

import math
"""A Magic class"""


class MagicClass:
    """A class that represents a geometric shape."""

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with an optional radius.

        Args:
            radius (float or int): The radius of the geometric shape.

        Raises:
            TypeError: If the provided radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the geometric shape."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the geometric shape."""
        return 2 * math.pi * self.__radius
