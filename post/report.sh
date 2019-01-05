#!/bin/bash
#
# Paul Evans
# 4 January 2018
# 4 May 2015
#
echo -n 'Sg case statements word count: '
wc -w ../hand/Gratian3.txt | awk '{print $1}'
echo -n 'Occurrences of "unde" in Sg case statements: '
cat ../hand/Gratian3.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bunde\b" | wc -l | awk '{print $1}'
echo -n 'Occurrences of "ergo" in Sg case statements: '
cat ../hand/Gratian3.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bergo\b" | wc -l | awk '{print $1}'
echo -n 'Occurrences of "igitur" in Sg case statements: '
cat ../hand/Gratian3.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bigitur\b" | wc -l | awk '{print $1}'
echo -n 'Occurrences of "quidem" in Sg case statements: '
cat ../hand/Gratian3.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bquidem\b" | wc -l | awk '{print $1}'
