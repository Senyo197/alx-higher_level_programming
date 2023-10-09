#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Checks whether or not object is subclass"""

    def area(self):
        """Area not implemented"""
        raise Exception("area() is not implemented")
