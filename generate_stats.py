''' cat source.csv | python3 generate_stats.py '''
import sys
import time
import collections
first = True
dist = collections.Counter()
max_values = 0
row_with_most_vowels = []

''' Compares passed string to max_vowels '''
def compare_vowels(string):
    global max_values
    vowels = 0
    for char in string:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                vowels = vowels + 1 
    if vowels > max_values:
        max_values = vowels
        return True
    else:
        return False


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

    ''' Update integer1 frequency '''
    integer1 = line[1]
    dist[integer1] += 1

    ''' Only waste time counting if len of string greater than most vowels, otherwise it can't be greater '''
    if len(line[2]) > max_values: 
        if compare_vowels(line[2]):
            row_with_most_vowels = line

    if len(line[3]) > max_values: 
        if compare_vowels(line[3]):
            row_with_most_vowels = line
        


print('[+] Distribution of Integer 1')
for k, v in dist.items():
    print(k, v)
print
print('[+] Row with most vowels: '),
print(row_with_most_vowels)

print("--- %s seconds ---" % (time.time() - start_time))
