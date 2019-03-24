import csv
import random
import string 
import os
import random

def generate_row(count):
    string1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    string2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,32)))
    data = [count, random.randint(1,10), string1, string2]
    return data

def manual3():
   outfile = 'data.csv'
   outsize = 50 #MB
   count = 0
   with open(outfile, 'w') as csvfile:
      wtr = csv.writer(csvfile)
      while (os.path.getsize(outfile)//1024**2) < outsize:
         wtr.writerow(generate_row(count)) 
         count += 1


manual3()
    

