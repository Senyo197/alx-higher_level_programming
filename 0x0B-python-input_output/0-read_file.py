#!/usr/bin/python3
"""Function to open a file"""


def read_file(filename=""):
    """Read a file"""
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                print(line, end='')
    except:
        pass
