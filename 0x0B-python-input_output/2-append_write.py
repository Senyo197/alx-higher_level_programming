#!/usr/bin/python3
"""A function to write into a file"""


def append_write(filename="", text=""):
    """Writes into a file"""
    try:
        with open(filename, 'a', encoding='UTF8') as file:
            content = file.write(text)
            return content
    except IOError:
        return -1
