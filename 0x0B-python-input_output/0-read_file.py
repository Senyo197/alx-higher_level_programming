#!/usr/bin/python3
"""Function to open a file"""


def read_file(filename=""):
    """Read a file"""
    try:
        with open(filename, 'r', encoding='UTF8') as file:
            read_content = file.read()
            print(read_content, end='')
    except:
        pass
