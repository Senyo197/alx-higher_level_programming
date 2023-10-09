#!/usr/bin/python
"""A list class"""


class MyList(list):
    """A sub class of list"""

    def print_sorted(self):
        """A sorted list function
        Prints:
            sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
