#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxival = 0
    maxikey = None
    for j, a in a_dictionary.items():
        if a > maxival:
            maxival = a
            maixval = j
    return maxikey
