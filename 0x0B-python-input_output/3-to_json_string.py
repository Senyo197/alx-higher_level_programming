#!/usr/bin/python3
"""Import json"""

import json

"""A function to return a json representation"""


def to_json_string(my_obj):
    """Returns a json representation"""
    json_string = json.dumps(my_obj)
    return json_string
