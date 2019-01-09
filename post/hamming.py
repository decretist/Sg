#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
# 12 December 2018
#
import re
import Levenshtein
import helper
def main():
    """
    Generate list of pairs of words, one from the Sg case statements,
    the other from the Friedberg edition, that differ by one
    character, e.g., "synodali" and "sinodali".
    """
    string = open('../hand/Gratian3.txt', 'r').read()
    string = re.sub('v', 'u', string)
    words = re.split(r'\W', string)
    sg_list = helper.listify(words)
    string = open('./tmp/detagged.txt', 'r').read()
    words = re.split(r'\W', string)
    fr_list = helper.listify(words)
    # deduplicate word lists using comprehensions
    sg_temp = [word for word in sg_list if word not in fr_list]
    fr_list = [word for word in fr_list if word not in sg_list]
    sg_list = sg_temp
    for sg_word in sg_list:
        for fr_word in fr_list:
            # ValueError: hamming expected two unicodes of the same length
            if len(sg_word) == len(fr_word):
                if Levenshtein.hamming(sg_word, fr_word) == 1:
                    print(sg_word, fr_word)

if __name__ == '__main__':
    main()
