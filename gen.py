import csv
import pandas as pd
import numpy as np
import random
import string 
import numpy as np
import uuid
import csv
import os
import multiprocessing


def generate_row(count):
    string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    data = [count, random.randint(1,10), string1, string2]
    return data

def first_try():
   count = 0
   with open('eggs.csv', 'w', newline='') as csvfile:
      while (os.path.getsize('eggs.csv')//1024**2) < 10:
         print((os.path.getsize('eggs.csv')//1024**2))
         writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         data = generate_row(count)
         writer.writerow(data)
         count +=1 

def numpy_try():
   result_array = np.array([])

   for i in range(0,10):
      result = generate_row(i)
      result_array = np.append(result, np.array([result]), axis=0)

   print(result_array)
   #np.savetxt("foo.csv", result_array, delimiter=",", fmt='%s')

def manual3():

   outfile = 'data.csv'
   outsize = 50# MB
   count = 0
   with open(outfile, 'w') as csvfile:
      wtr = csv.writer(csvfile)
      while (os.path.getsize(outfile)//1024**2) < outsize:
         wtr.writerow(generate_row(count)) 
         count += 1


manual3()
    

