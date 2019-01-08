#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
# 12 December 2018
#
"""
Helper functions to created sorted lists of unique words
and dictionaries of word-frequency pairs.
"""
def dictify(words):
    """Return a dictionary of words with frequencies."""
    word_freq = {}
    for word in words:
        if word:
            key = word.lower()
            if key in word_freq:
                word_freq[key] += 1
            else:
                word_freq[key] = 1
        else:
            pass
    return word_freq

def listify(words):
    """Return a sorted list of unique words."""
    word_list = []
    for word in words:
        if word:
            word = word.lower()
            if word not in word_list: # add it
                word_list.append(word)
        else:
            pass
    word_list.sort()
    return word_list
