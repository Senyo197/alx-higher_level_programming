#!/usr/bin/python
"""Defines a class to determine a subclass"""


def is_same_class(obj, a_class):
    """Checks whether or not object is subclass"""
    if type(obj) == a_class:
        return True
    return False
