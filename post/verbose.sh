#!/bin/bash
#
# Paul Evans
#  8 Jan 2019
#
# Determine whether the case statements in Sg are more verbose than
# the corresponding ones in the vulgate (Friedberg) Decretum.
#
# non-xque version of vulgate (Friedberg) case statements
# FR_FILE=~/Work/Gratian/samples/hand/Gratian0.txt
# FR_FILE=~/Work/Gratian/stylometry/corpora/corpus6/Gratian0.txt
FR_FILE=./tmp/Gratian0.txt
SG_FILE=../hand/Gratian3.txt
# Remove C.24, 25, 26, and 28 from vulgate (Friedberg) case statements
sed '24,26d;28d' $FR_FILE > tmp/fr.txt
# Remove Causa Prima from Sg case statements
sed '1d' $SG_FILE > tmp/sg.txt
echo -e -n "Fr.:\t"
wc -w tmp/fr.txt | awk '{print $1}'
echo -e -n "Sg:\t"
wc -w tmp/sg.txt | awk '{print $1}'
