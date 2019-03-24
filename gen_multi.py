from queue import Queue
import os
import random
import string
from threading import Thread
import time
import itertools
import csv
q = Queue()
outfile = 'data.csv'
outsize = 1 # MB
file = open(outfile, 'w')
wtr = csv.writer(file)

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def generate_row(count):
    string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    data = [str(count), str(random.randint(1,10)), string1, string2]
    #return ','.join(data) + '\n'
    return data

def make_rows():
    count = 0
    while (os.path.getsize(outfile)//1000000) < outsize:
    #while count < 100000:
        q.put(generate_row(count))
        count = count + 1

def write_file():
   while not q.empty():
       wtr.writerow(q.get())
       #print(q.get())


if __name__ == '__main__':
    Thread(target = make_rows).start()
    Thread(target = write_file).start()
    
