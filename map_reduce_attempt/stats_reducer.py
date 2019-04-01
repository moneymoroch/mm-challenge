'''
Attempt to count vowels by creating catching input from stats_mapper.py
cat source.csv | python3 stats_mapper.py | python3 stats_reducer.py
'''
#!/usr/bin/env python3
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


if __name__ == '__main__':
    max_vowels = 0
    row_with_most_vowels = []
    for line in sys.stdin:
        #print(line)
        line = line.rstrip()
        row, count= line.split(',')
        count = int(count)
        
        if int(count) > max_vowels:
            row_with_most_vowels, max_vowels = row, count
  
  
    print(row_with_most_vowels)
