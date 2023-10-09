#!/usr/bin/python3
"""Defines a class to determine an instance"""


def is_kind_of_class(obj, a_class):
    """Checks whether or not object is instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
