#!/usr/bin/python3
"""Defines an integer addition function.
Float arguments are typecated into int before addition.
Raises:
    TypeError: If either of a or b is non-float or non-int
"""


def add_integer(a, b=98):
    """Return an addition of a and b
    Float arguments are typecated into int before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
