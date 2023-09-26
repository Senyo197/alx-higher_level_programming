#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        int_value = int(value)
        sys.stdout.write("{:d}\n".format(int_value))
        return True
    except ValueError as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
