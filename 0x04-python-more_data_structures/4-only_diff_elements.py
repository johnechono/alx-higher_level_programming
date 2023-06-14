#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_new = set_2.difference(set_1)
    set_new.update(set_1.difference(set_2))
    return (set_new)
