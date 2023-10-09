#!/usr/bin/python
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """A sorted list function
        Prints:
            sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
