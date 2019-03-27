'''
Attempt to count vowels by creating catching input from mapper.py
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
    max_vowels_row = []
    for row in data:
        v_count = count_vowels(row[2])
        if v_count > max_vowels:
            max_vowels = v_count
            max_vowels_row = row

    print(row)



if __name__ == '__main__':
    max_vowels = 0
    row_with_most_vowels = []
    for line in sys.stdin:
        
        line = line.strip()
        line = line.split(",")

        if len(line[2]) > max_vowels: 
            if count_vowels(line[2]) > max_vowels:
                row_with_most_vowels = line

        if len(line[3]) > max_vowels: 
            if count_vowels(line[3]) > max_vowels:
                row_with_most_vowels = line


  
  
    print(row_with_most_vowels)