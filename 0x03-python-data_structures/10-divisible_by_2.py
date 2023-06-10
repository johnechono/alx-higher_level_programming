#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    divisibility = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisibility.append(True)
        else:
            divisibility.append(False)
    return (divisibility)
