#!/usr/bin/python3
"""A look-up function"""


def lookup(obj):
    """Returns a list of available attributes and methods
    Args:
        obj (object): The object for which you want to retrieve
    Returns:
        list: A list of attribute and method names.
    """
    attr_and_method = []
    for attr in dir(obj):
        if not attr.startswith("__"):
            if not callable(getattr(obj, attr)):
                attr_and_method.append(attr)
            else:
                attr_and_method.append(attr)
    return attr_and_method
