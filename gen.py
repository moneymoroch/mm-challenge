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
      self.outfile = 'source.csv'
      self.outsize = 10 # In Megabytes
      self.rowcount = 0
      self.firstrow = True


   ''' Simple utility function to generate a row of data in specified format '''
   def generate_row(self, count):
      string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
      data = [str(self.rowcount), str(random.randint(1,10)), string1, string2]
      return data


   ''' Most Simple Implementation using CSV writer '''
   def simple_generate_file(self):
      
      ''' Open File and Use CSV Writer module'''
      with open(self.outfile, 'w') as csvfile:
         wtr = csv.writer(csvfile)

         ''' Write header row '''
         if self.firstrow:
            wtr.writerow(['id', 'integer1', 'string1', 'string2']) 
            self.firstrow = False

         ''' If current file size less than desired size, keep generating data and write to row '''
         while (os.path.getsize(self.outfile)//1024**2) < self.outsize:
            wtr.writerow(self.generate_row(self.rowcount)) 
            self.rowcount += 1
   

   ''' Attempt to speed up writes by batching them ''' 
   def generate_file_in_chunks(self):
      buffer = ''
      with open(self.outfile, 'w') as file:
         while (os.path.getsize(self.outfile)//2**20) < self.outsize:
             
            ''' Write header row '''
            if self.firstrow:
               file.write('id,integer1,string1,string2\n') 
               self.firstrow = False

            data = self.generate_row(self.rowcount)
            buffer += ','.join(data) + '\n'
            self.rowcount += 1
            
            ''' After rowcount reaches threshold, make bulk write '''
            if self.rowcount % 10000 == 0:
               #print('Batch Writing')
               file.write(buffer)
               buffer = ''


   ''' Function that uses stdout to write to file.
       This is sort of odd, but I noticed some speed up for small 
       file sizes. 
   '''
   def generate_pipe_output(self):

      ''' Set stdout to file, anything printed will br written to file '''
      sys.stdout = open(self.outfile, 'w')

      ''' Loop until file is bigger than desired outside '''
      while (os.path.getsize(self.outfile)//2**20) < self.outsize:
         
         ''' Write header row '''
         if self.firstrow:
            print('id,integer1,string1,string2') 
            self.firstrow = False

         data = self.generate_row(self.rowcount)
         print(','.join(data))
         self.rowcount += 1
      
      ''' Reset STD OUT to normal default '''
      sys.stdout = sys.__stdout__
      

            
if __name__ == '__main__':
   print("Generating File...")
   start_time = time.time()

   mm = MMChallenge()
   mm.generate_file_in_chunks()

   print("--- %s seconds ---" % (time.time() - start_time))

