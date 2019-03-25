from queue import Queue
import os
import random
import string
from threading import Thread
import time
import itertools
import csv
import sys
import multiprocessing

''' Shared boolean among processes '''
finished = multiprocessing.Value('i', False)

class MMChallengeProcessing:
    def __init__(self):
        self.jobs = multiprocessing.Queue()
        self.outfile = 'source.csv'
        self.outsize = 100 # MB
        self.file = open(self.outfile, 'w')
    
        self.start = 0
        self.end = 2000
        self.offset = 2000

    ''' Function to generate row specified in document, returns string with newline '''
    def generateRow(self, count):
        string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        data = [str(count), str(random.randint(1,10)), string1, string2]
        return ','.join(data) + '\n'


    ''' Generates and writes data for range of primary keys given. For example, if 2000, 4000 are used, 
        function will generate 2000 rows starting with id 2000 and ending at 40000. 
    '''
    def calculateAndWrite(self, start, end):
            temp = ''
            for index in range(start, end):
                temp += (self.generateRow(index))
            self.file.write(temp)

    ''' Pops jobs off queue to process '''     
    def processJobs(self, jobs):
        while not self.jobs.empty() and not bool(finished.value):
            window = self.jobs.get()
            start, end = window
            self.calculateAndWrite(start, end)


    ''' Worker that will continuosly add chunks of primary id's to calculate until file size if reached '''
    def loadJobs(self):
        while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
                self.jobs.put([self.start, self.end])
                self.start = self.end 
                self.end += self.offset

        with finished.get_lock():
            finished.value = True

        print("--- %s seconds ---" % (time.time() - start_time))
        sys.exit()

    ''' Main function '''
    def run(self):
        t = multiprocessing.Process(target=self.loadJobs, args=())
        t.start()
        numProcesses = 30
        for work in range(0, numProcesses):
            worker = multiprocessing.Process(target=self.processJobs, args=(self.jobs,))
            worker.start()
            worker.join()
           
        
if __name__ == '__main__':
    print("Generating File...")
    start_time = time.time()

    mm = MMChallengeProcessing()
    mm.run()
   

   
    
