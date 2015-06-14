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


def mutate(source):
    """Mutates our source string by one char.
    We use a simple mutation of changing one either up a character or down
    a character.

    Keyword arguments:
    source -- the string we will be mutating
    """
    charpos = random.randint(0, len(source) - 1)
    string_parts = list(source)
    # We use a random character to mutate and then offset it by 1, -1 or 0 to
    # get our mutated string
    string_parts[charpos] = chr(ord(string_parts[charpos]) +
                                random.randint(-1, 1))
    return ''.join(string_parts)


# Our starting string
source = "at!Ph;afn23Xc"
# Our desired string
target = "Hello, World!"

# Getting the initial fitness value of our string
fitval = fitness(source, target)
i = 0
while True:
    i += 1
    # Mutate our string
    mutation = mutate(source)
    # The fitness value of our mutated string
    mutatedFitval = fitness(mutation, target)
    # If the fitness value of our mutated string is better than our previous
    # fitness value (lower) make that our new source because it is closer to
    # the target value.
    if mutatedFitval < fitval:
        fitval = mutatedFitval
        source = mutation
        print "%5i %5i %14s" % (i, mutatedFitval, mutation)
    if fitval == 0:
        break
