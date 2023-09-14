#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use set() to get unique elements, then use sum() to calculate the sum
    return sum(set(my_list))
