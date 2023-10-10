#!/usr/bin/python3
"""Import Json"""

import json
"""A function definition to write into a file with json"""


def save_to_json_file(my_obj, filename):
    """Writes into a file with json"""
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(my_obj, file, indent=4, ensure_ascii=False)
