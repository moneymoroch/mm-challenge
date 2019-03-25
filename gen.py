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
      self.outsize = 100 # In Megabytes
      self.rowcount = 0
      self.firstrow = False


   ''' Simple utility function to generate a row of data in specified format '''
   def generate_row(self, count, return_type='list'):
      string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      data = [str(self.rowcount), str(random.randint(1,10)), string1, string2]

      if return_type == 'list':
         return data
      else:
         return ','.join(data)


   ''' Most Simple Implementation using CSV writer '''
   def simple_generate_file(self):
      ''' Open File and Use CSV Writer module'''
      with open(self.outfile, 'w') as csvfile:
         wtr = csv.writer(csvfile)

         ''' If current file size less than desired size, keep generating data and write to row '''
         while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
            wtr.writerow(self.generate_row(self.rowcount)) 
            self.rowcount += 1
   

   ''' Attempt to speed up writes by batching them ''' 
   def generate_file_in_chunks(self):
      temp = ''
      with open(self.outfile, 'w') as file:
         while (os.path.getsize(self.outfile)//2**20) < self.outsize:

            temp += self.generate_row(self.rowcount)
            self.rowcount += 1
            
            ''' After rowcount reaches threshold, make bulk write '''
            if self.rowcount % 10000 == 0:
               print('writing')
               file.write(temp)
               temp = ''


   ''' Function that iteratively loops to create data and pipes output to file '''
   def generate_pipe_output(self):

      ''' Set stdout to file '''
      sys.stdout = open(self.outfile, 'w')

      ''' Loop until file is bigger than desired outside '''
      while (os.path.getsize(self.outfile)//2**20) < self.outsize:
         print(self.generate_row(self.rowcount))
         self.rowcount += 1
      
      ''' Reset STD OUT to normal default '''
      sys.stdout = sys.__stdout__
      

            
if __name__ == '__main__':
   print("Generating File...")
   start_time = time.time()

   mm = MMChallenge()
   mm.simple_generate_file()

   print("--- %s seconds ---" % (time.time() - start_time))

