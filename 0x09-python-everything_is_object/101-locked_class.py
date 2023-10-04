#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating new objects but one named 'first_name'.
    """
    __slots__ = ["first_name"]
