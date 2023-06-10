#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list is None:
        return (None)

    if len(my_list) == 0:
        return (None)

    max = my_list[0]
    for j in my_list:
        if j > max:
            max = j
    return (max)
