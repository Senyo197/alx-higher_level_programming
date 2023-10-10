#!/usr/bin/python3
"""Import json"""

import json

"""A function to return a json representation"""


def from_json_string(my_str):
    """Returns a json representation"""
    my_obj = json.loads(my_str)
    return my_obj
