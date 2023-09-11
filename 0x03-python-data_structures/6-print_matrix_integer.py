#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for num in row:
            fmt = "{:d}".format(num)
            print(fmt, end= " " if num != row[-1] else "")
        print()
