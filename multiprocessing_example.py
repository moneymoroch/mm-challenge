'''
0,1,ejhscz,pkizppftralthlzzspfobywktishpdzs
1,2,eagkrzkpyqv,zsxlplnnagmkbbssniv
2,4,twieejamnrnawmhgomxsjgfiz,ygqbf
3,10,rohwp,jjxbxlbzjeyjdjnscybpsezel
4,4,telmbeeassdakvkixgivypka,xklsnjrzqspe
5,7,enwrdzyk,s
6,5,xbebvexptrgn,ztxbxnsxjvuolxellsthyxhrnvmpmr
7,5,cygdkkgihf,svowxsfl
8,2,gpnibbtftepqieoxk,mchjasdlmrzptnqakqjvmxfeinsob
9,3,tmxwwpnu,rjtk
10,10,ucrvtiichoflgrfthicbmejy,qfpjhetpeq
'''

from queue import Queue
import os
import random
import string
import time
import itertools
import multiprocessing

exit_flag = multiprocessing.Value('i', 0)

last_line = multiprocessing.Value('i', 0)

jobqueue = multiprocessing.Queue()
start = 0
end = 10
offset = 10
lock = multiprocessing.Lock()

def calculateAndWrite(start, end):
    
    ''' Get process ID '''
    pid = multiprocessing.current_process()._identity[0]

    while True:
        if last_line.value == start:
            print('Process {}: Writing Lines {} to {}'.format(pid, start, end))
            last_line.value = end
            return
        else:
            print('Process {}: Current last line {}, Waiting..'.format(pid, last_line.value))

        time.sleep(1)
        
''' Pops jobs off queue to process '''     
def processJobs(jobs):
    while True:
        window = jobqueue.get()
        start, end = window
        calculateAndWrite(start, end)
        if exit_flag.value == 1:
            break


''' Worker that will continuously add chunks of primary id's to calculate until file size is reached '''
def loadJobs(lock):
    global start, end
    while True:
        jobqueue.put([start, end])
        start = end 
        end += offset



''' Start pushing jobs to queue '''
t = multiprocessing.Process(target=loadJobs, args=(lock, ))
t.start()


''' Process jobs and write to file '''
numProcesses = 5
for work in range(0, numProcesses):
    worker = multiprocessing.Process(target=processJobs, args=(jobqueue,))
    worker.start()
    
    

   
    
