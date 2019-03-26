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

''' Shared variable among processes to signal program termination '''
exit_flag = multiprocessing.Value('i', 0)

class MMChallengeProcessing:
    def __init__(self):
        self.jobqueue = multiprocessing.Queue()
        self.outfile = 'source.csv'
        self.outsize = 10 # MB
        self.file = open(self.outfile, 'w')
    
        self.start = 0
        self.end = 2000
        self.offset = 2000
        self.lock = multiprocessing.Lock()

    ''' Function to generate row specified in document, returns string with newline '''
    def generateRow(self, count):
        string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
        data = [str(count), str(random.randint(1,10)), string1, string2]
        return ','.join(data) + '\n'


    ''' Generates and writes data for range of primary keys given. For example, if 2000, 4000 are passed as arguments, 
        function will generate 2000 rows starting with id 2000 and ending at 4000. 
    '''
    def calculateAndWrite(self, start, end):
            temp = ''
            for index in range(start, end):
                temp += (self.generateRow(index))
            self.file.write(temp)

    ''' Pops jobs off queue to process '''     
    def processJobs(self, jobs):
        while True:
            window = self.jobqueue.get()
            start, end = window
            self.calculateAndWrite(start, end)
            if exit_flag.value == 1:
                break


    ''' Worker that will continuously add chunks of primary id's to calculate until file size is reached '''
    def loadJobs(self, lock):
        while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
                self.jobqueue.put([self.start, self.end])
                self.start = self.end 
                self.end += self.offset

        
        print("--- %s seconds ---" % (time.time() - start_time))

        print("Cleaning up queue to exit")
        with multiprocessing.Lock():
            exit_flag.value += 1
            while not self.jobqueue.empty():
                self.jobqueue.get()
    
        ''' Close file '''
        self.file.close()

    ''' Main function '''
    def run(self):

        ''' Write Header Row '''
        self.file.write('id,integer1,string1,string2\n') 

        ''' Start pushing jobs to queue '''
        t = multiprocessing.Process(target=self.loadJobs, args=(self.lock, ))
        t.start()
        
        ''' Process jobs and write to file '''
        numProcesses = 25
        for work in range(0, numProcesses):
            worker = multiprocessing.Process(target=self.processJobs, args=(self.jobqueue,))
            worker.start()
            worker.join()
           
        
if __name__ == '__main__':
    print("Generating File...")
    start_time = time.time()

    mm = MMChallengeProcessing()
    mm.run()
   

   
    
