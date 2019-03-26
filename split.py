import gzip
import os
import math
import time 

class MMSplitter:

    ''' Set source file and get file size '''
    def __init__(self):
        self.source_file = 'source.csv.gz'
        self.source_file_size = os.path.getsize(self.source_file)
        self.num_files = 10


    def split_file(self):

        ''' Calculate sizes of new files (source size / number of splits)'''
        chunk_size = math.ceil(self.source_file_size/10)
       
        with gzip.open(self.source_file, 'rb') as source:
            for chunk in range(1, (self.num_files + 1)):
                fname = '{}.csv.gz'.format(chunk)
                print('Writing {}'.format(fname))

                ''' Open Nth file and write next chunk '''
                with gzip.open(fname,'wb') as newfile:
                    newfile.write(source.read(chunk_size))
                

if __name__ == '__main__':
    print("Splitting File...")
    start_time = time.time()

    splitter = MMSplitter()
    splitter.split_file()

    print("--- %s seconds ---" % (time.time() - start_time))