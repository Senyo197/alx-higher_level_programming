#!/usr/bin/python3
"""Defines a class to determine a subclass"""


def inherits_from(obj, a_class):
    """Checks whether or not object is subclass"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
