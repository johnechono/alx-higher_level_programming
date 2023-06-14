#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_new = []

    for i in my_list:
        if i not in list_new:
            list_new.append(i)
    return sum(list_new)
