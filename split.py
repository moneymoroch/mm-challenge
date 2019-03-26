import gzip
import os
import math

class MMSplitter:

    ''' Set source file and get file size '''
    def __init__(self):
        self.source_file = 'source.csv.gz'
        self.source_file_size = os.path.getsize(self.source_file)


    def split_file(self):

        ''' Calculate sizes of new files (source size / number of splits)'''
        chunk_size = math.ceil(self.source_file_size/10)
       
        with gzip.open(self.source_file, 'rb') as source:
            for chunk in range(1, 11):
                fname = '{}.csv.gz'.format(chunk)
                print('Writing {}'.format(fname))

                with gzip.open(fname,'wb') as newfile:
                    newfile.write(source.read(chunk_size))
                

if __name__ == '__main__':
    splitter = MMSplitter()
    splitter.split_file()