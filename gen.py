import csv
import random
import string 
import os
import random
import time 
import sys

class MMChallenge:

   ''' Constructor '''
   def __init__(self):
      self.outfile = 'data.csv'
      self.outsize = 10 # In MegaBytes
      self.rowcount = 0
      self.firstrow = False

   ''' Simple function to generate a row of data in specified format '''
   def generateRow(self, count, return_type='string'):
      string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      data = [str(self.rowcount), str(random.randint(1,10)), string1, string2]

      if return_type == 'array':
         return data
      else:
         return ','.join(data)

   ''' Most Simple Implementation '''
   def generateFile(self):
      ''' Open File and Use CSV Writer module'''
      with open(self.outfile, 'w') as csvfile:
         wtr = csv.writer(csvfile)

         ''' If current file size less than desired size, generate and write to row '''
         while (os.path.getsize(self.outfile)//2^20) < self.outsize:
            wtr.writerow(self.generateRow(self.rowcount)) 
            self.rowcount += 1
   
   def generateFileInChunks(self):
      ''' Open file and append string with new line '''
      temp = ''
      with open(self.outfile, 'w') as file:
         while (os.path.getsize(self.outfile)//2**20) < self.outsize:

            temp += self.generateRow(self.rowcount)
            self.rowcount += 1
            
            ''' After rowcount reaches threshold, make bulk write '''
            if self.rowcount % 100000 == 0:
               print('writing')
               file.write(temp)
               temp = ''

   def pipeOutput(self):

      ''' Set stdout to file '''
      sys.stdout = open(self.outfile, 'w')

      ''' Loop until file is bigger than desired outside '''
      while (os.path.getsize(self.outfile)//2**20) < self.outsize:
         print(self.generateRow(self.rowcount))
         self.rowcount += 1
      

            

      

start_time = time.time()

mm = MMChallenge()
mm.pipeOutput()
sys.stdout = sys.__stdout__
print("--- %s seconds ---" % (time.time() - start_time))

