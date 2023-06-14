#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return (None)
    key_best = None
    score_best = 0
    for key, value in a_dictionary.items():
        if value > score_best:
            score_best = value
            key_best = key
    return (key_best)
