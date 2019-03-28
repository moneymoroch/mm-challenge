#!/usr/bin/env python3
'''
Attemt to speed up calculation of vowel count by simulating a mapreduce job. 

To run on HDFS:

bin/hadoop jar /usr/local/Cellar/hadoop/3.1.1/libexec/share/hadoop/tools/lib/hadoop-*streaming*.jar -D mapred.reduce.tasks=16 \
-file /Users/zuba/mm-challenge/map_reduce_attempt/stats_mapper.py \
-mapper  'python3 stats_mapper.py'  \
-file  /Users/zuba/mm-challenge/map_reduce_attempt/stats_reducer.py  \
-reducer 'python3 stats_reducer.py'  \
-input /user/zuba/source/source.csv \
-output /user/zuba/source/output


cat source.csv | python3 map_reduce_attempt/stats_mapper.py | python3 map_reduce_attempt/stats_reducer.py
'''
import sys
import time
import collections
import multiprocessing
first = True

def count_vowels(string):
    vowels = 0
    for char in string:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                vowels = vowels + 1 

    return vowels

def process_chunk(data):
    max_vowels = 0
    row_with_most_vowels = []
    for row in data:
        if len(row[2]) > max_vowels: 
            if count_vowels(line[2]) > max_vowels:
                row_with_most_vowels = line

        if len(row[3]) > max_vowels: 
            if count_vowels(line[3]) > max_vowels:
                row_with_most_vowels = line

    print(",".join(row_with_most_vowels))

if __name__ == '__main__':
    linecount = 0
    data = []

    for line in sys.stdin:
        ''' Skip Header Row '''
        if first:
            first = False
            continue

        ''' Strip data '''
        line = line.strip()
        line = line.split(",")
        data.append(line)  
        linecount += 1

        if linecount == 5000:
            linecount = 0
            process_chunk(data)
            #multiprocessing.Process(target=process_chunk, args=(data,)).start()
            data = []

