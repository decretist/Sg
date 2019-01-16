#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
#
import re
import helper
def main():
    # string = open('../hand/Gratian3.txt', 'r').read()
    string = open('./FrSpell.txt', 'r').read()
    words = re.split(r'\W', string)
    sg_freqs = helper.dictify(words)
    string = open('../tmp/detagged.txt', 'r').read()
    words = re.split(r'\W', string)
    fr_freqs = helper.dictify(words)
    # Words in Sg case statements and not in edF
    keys = sg_freqs.keys()
    for key in keys:
        if key in sg_freqs and key not in fr_freqs:
            print("%2d\t%s" % (sg_freqs[key], key))

if __name__ == '__main__':
    main()
