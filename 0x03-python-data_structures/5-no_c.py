#!/usr/bin/python3

def no_c(my_string):

    filtered_list = []

    for char in my_string:
        if char != 'c' and char != 'C':
            filtered_list.append(char)

    new_string = ''.join(filtered_list)
    return new_string
