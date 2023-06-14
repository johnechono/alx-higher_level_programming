#!/usr/bin/python3

def weight_average(my_list=[]):

    if len(my_list) == 0:
        return (0)
    score_sum = 0
    weight_sum = 0

    for i in my_list:
        score_sum += i[0] * i[1]
        weight_sum += i[1]
    return (score_sum / weight_sum)
