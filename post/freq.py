#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
#
import re
import helper
def main():
    """freq.py | sort -n -r | head -300 | awk '{print $2}' | sort > freq.out"""
    string = open('../hand/Gratian3.txt', 'r').read()
    words = re.split(r'\W', string)
    sg_freqs = helper.dictify(words)
    keys = sg_freqs.keys()
    for key in keys:
        # print("%2d\t%s" % (sg_freqs[key], key))
        # print("{:2d}\t{}".format(sg_freqs[key], key))
        print(f'{sg_freqs[key]:2d}\t{key:s}')

if __name__ == '__main__':
    main()
