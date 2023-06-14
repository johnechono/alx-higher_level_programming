#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = []
    for i in my_list:
        if i == search:
            list_new.append(replace)
        else:
            list_new.append(i)
    return (list_new)
