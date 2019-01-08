#!/usr/local/bin/python3
#
# Paul Evans
# 7 January 2019
#
import hashlib
import urllib.request
import sys
def main():
    '''
    Opens a file directly from a GitHub repository, verifies its
    contents using an SHA1 message digest, and caches a local copy.
    '''
    github = 'https://raw.githubusercontent.com/decretist/Gratian/master/'
    # path = 'stylometry/corpora/corpus6/Gratian0.txt'
    path = 'samples/hand/Gratian0.txt'
    digest = '50e84f9fa789036c9ae4be9f0d5ecbded4969bae'
    string = urllib.request.urlopen(github + path).read()
    print(hashlib.sha1(string).hexdigest(), file=sys.stderr)
    if digest == hashlib.sha1(string).hexdigest():
        filename = open('./tmp/Gratian0.txt', 'w')
        filename.write(string.decode())
        print(string.decode().strip())

if __name__ == "__main__":
    main()
