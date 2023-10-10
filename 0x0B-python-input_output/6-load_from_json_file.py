#!/usr/bin/python3
"""Import Json"""

import json
"""A function definition to load from a json file"""


def load_from_json_file(filename):
    """Loading from json file"""
    with open(filename, 'r', encoding='UTF8') as file:
        my_obj = json.load(file)
        return my_obj
