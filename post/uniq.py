#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
#  7 Jan 2019
# 13 Dec 2018
#
import re
import helper
def main():
    '''
    Prints list of words that occur in Sg case statements and not
    in Fr. case statements:
    uniq.py | sort -n -r | head -12
    '''
    string = open('../hand/Gratian3.txt', 'r').read()
    string = re.sub('v', 'u', string)
    words = re.split(r'\W', string)
    sg_freqs = helper.dictify(words)
    string = open('./tmp/Gratian0.txt', 'r').read()
    words = re.split(r'\W', string)
    fr_freqs = helper.dictify(words)
    keys = sg_freqs.keys()
    for key in keys:
        if key in sg_freqs and key not in fr_freqs:
            # print("%2d\t%s" % (sg_freqs[key], key))
            # print("{:2d}\t{}".format(sg_freqs[key], key))
            print(f'{sg_freqs[key]:2d}\t{key:s}')

if __name__ == '__main__':
    main()
