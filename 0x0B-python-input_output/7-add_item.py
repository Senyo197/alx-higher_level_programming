#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    arguments = sys.argv[1:]

    existing_data.extend(arguments)

    save_to_json_file(existing_data, "add_item.json")
