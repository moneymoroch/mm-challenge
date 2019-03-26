'''
Program takes piped input from source.csv and calculates specified stats
To run:
    cat source.csv | python3 generate_stats.py
    
'''
import sys
import time
import collections

''' Global vars to be updated '''
first = True ## Set to False after header row passed
dist = collections.Counter() ## Used to build integer distribution
max_vowels = 0
row_with_most_vowels = []


''' Compares passed string to max_vowels '''
def compare_vowels(string):
    global max_vowels
    vowels = 0
    for char in string:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                vowels = vowels + 1 
    if vowels > max_vowels:
        max_vowels = vowels
        return True
    else:
        return False

''' Print summary of data '''
def print_summary():
    print('-------------------------------')
    print('[+] Distribution of Integer 1')
    for k, v in dist.items():
        print('{}: {}'.format(k,v))
    print('-------------------------------\n')
    print('[+] Row with most vowels: {} '.format(row_with_most_vowels[0]))
    print(row_with_most_vowels)
    print('-------------------------------\n')


if __name__ == '__main__':
    start_time = time.time()

    ''' Loop through piped input '''
    for line in sys.stdin:

        ''' Skip Header Row '''
        if first:
            first = False
            continue

        ''' Strip data '''
        line = line.strip()
        line = line.split(",")

        ''' Update integer1 frequency using collections.Counter()'''
        integer1 = line[1]
        dist[integer1] += 1

        ''' If length of string less than max_vowels, 
            dont waste time computing since it cant be greater even if all vowels'''
        if len(line[2]) > max_vowels: 
            if compare_vowels(line[2]):
                row_with_most_vowels = line

        if len(line[3]) > max_vowels: 
            if compare_vowels(line[3]):
                row_with_most_vowels = line
            
    print_summary()
    print("--- %s seconds ---" % (time.time() - start_time))
