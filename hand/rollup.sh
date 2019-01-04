#!/bin/bash
#
# Paul Evans
#  4 January 2018
# 25 October 2015
#
if [ -f Gratian3.txt ];
then
    rm -i Gratian3.txt
fi
while read -r line
do
    file=cases/"Sg $line".txt
    cat "$file" >> Gratian3.txt
done < toc_cases.txt
shasum -c Gratian3.sha1
