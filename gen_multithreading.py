'''
Ignore this file, still a work in progress

'''

from queue import Queue
import os
import random
import string
from threading import Thread
import time
import itertools
import csv
import sys

class MMChallengeThreading:
    def __init__(self):
        self.q = Queue()
        self.outfile = 'source.csv'
        self.outsize = 10 # MB
        self.file = open(self.outfile, 'w')
        self.finished = False
        self.start = 0
        self.end = 1000
        self.offset = 1000

    def generateRow(self, count):
        string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        data = [str(count), str(random.randint(1,10)), string1, string2]
        return ','.join(data) + '\n'

    def makeRows(self, start, end):
        temp = ''
        for i in range(start, end):
            temp += (self.generateRow(i))
        self.file.write(temp)

    def run(self):
        while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
                t = Thread(target = self.makeRows, args=(self.start, self.end,))
                self.start = self.end 
                self.end += self.offset
                t.daemon = True
                t.start()
        
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    print("Generating File...")
    start_time = time.time()

    mm = MMChallengeThreading()
    mm.run()
    

   
    
