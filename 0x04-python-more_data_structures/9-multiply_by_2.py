#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_new = a_dictionary.copy()
    for key in dict_new.keys():
        dict_new[key] = dict_new[key] * 2
    return (dict_new)
