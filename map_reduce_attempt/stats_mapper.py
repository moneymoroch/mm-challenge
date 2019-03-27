'''
cat source.csv | python3 stats_mapper.py | python3 stats_reducer.py
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

def processChunk(data):
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
            processChunk(data)
            multiprocessing.Process(target=processChunk, args=(data,)).start()
            data = []

