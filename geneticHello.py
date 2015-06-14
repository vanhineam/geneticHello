#!/usr/bin/python

import random

def fitness(source, target):
    """Determines the fitness score of our string.

    Keyword arguments:
    source -- the string we will be testing the fitness of
    target -- the string we will be using as our goal
    """
    fitval = 0
    # For each character in our string, compare the numeric value of each
    # character to our target strings character. We square it to get rid of any
    # negative numbers
    for i in range(0, len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return fitval

