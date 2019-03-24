from queue import Queue
import os
import random
import string
from threading import Thread
import time
import itertools
import csv
import sys

class MMChallengeThreaded:
    def __init__(self):
        self.q = Queue()
        self.outfile = 'data.csv'
        self.outsize = 50 # MB
        self.file = open(self.outfile, 'w')
        self.finished = False
        self.start = 0
        self.end = 10000
        self.offset = 10000

    def getSize(self, filename):
        st = os.stat(filename)
        return st.st_size

    def generateRow(self, count):
        string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        data = [str(count), str(random.randint(1,10)), string1, string2]
        return ','.join(data) + '\n'
        #return data

    def makeRows(self, start, end):
        temp = ''
        for i in range(start, end):
            temp += (self.generateRow(i))
        self.file.write(temp)


    def writeStream(self):
        ''' Set stdout to file '''
        sys.stdout = open(self.outfile, 'w')

        with open(self.outfile, 'w') as self.file:
            while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
                while not self.q.empty():
                    print(self.q.get())

        self.finished = True
        sys.stdout = sys.__stdout__
        print("--- %s seconds ---" % (time.time() - start_time))
        cleanup_stop_thread()
        sys.exit()

    def run(self):

        while (os.path.getsize(self.outfile)//1024**2) < self.outsize:

                print('starting thread')
                print(self.start, self.offset)
                t = Thread(target = self.makeRows, args=(self.start, self.end,))
                self.start = self.end 
                self.end += self.end
                t.start()
                
        print("--- %s seconds ---" % (time.time() - start_time))

    def collect(self):
        Thread(target = self.writeStream, args=(self.start, self.offset,))

if __name__ == '__main__':
    start_time = time.time()

    mm = MMChallengeThreaded()
    mm.run()
    mm.collect()
    

   
    
