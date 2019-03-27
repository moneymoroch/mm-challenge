# mm-challenge
```
git clone https://github.com/moneymoroch/mm-challenge.git
cd mm-challenge
python3 gen.py
cat source.csv | python3 generate_stats.py
gzip -f source.csv
python3 split.py
```

## Questions

### How many rows did you generate? Why?

23599999 rows

The program gen.py writes rows dynamically based on the current file size until the desired size is reached. Thus the amount of rows will almost always be different each run since the contents of the rows are random. 


### What is the content of the last row? How can you easily find this?
From linux/mac command line
```
tail -n 1 source.csv 
23599999,9,ndyqaf,kmti
```

### What is the distribution of integer1? Which is most common?
Most common is 8 with 2363023 occurences, from summary of program output
``` 
cat source.csv | python3 generate_stats.py
 
int1, frequency
(8, 2363023)
(4, 2361778)
(9, 2359985)
(2, 2358769)
(5, 2356318)
(3, 2357820)
(1, 2361097)
(10, 2359610)
(7, 2362930)
(6, 2358670)
```

###  Which row has the most vowels (considering Columns string1 and string2)?

From summary of program output, row 12819653 has the most vowels with the string 'oidohxaoouaoteeodasnaeeywbutvooa'
 ``` 
 cat source.csv | python3 generate_stats.py 

 ['12819653', '9', 'oidohxaoouaoteeodasnaeeywbutvooa', 'ihhxcucpgeeywzejsrammwwbainj']
 ```
Row 12819653 has the most vowels with the string 'oidohxaoouaoteeodasnaeeywbutvooa'


### How large is a compressed (gzip) version of this file? 

606 MB
```
du -h source.csv.gz 
606M	source.csv.gz
```

### How long did the compression process take?
Around 1 minute
```
time gzip -f source.csv
real	1m2.844s
user	1m1.473s
sys	0m0.916s
```

### How long does splitting the compressed file take?
81 seconds
```
python3 split.py 
Splitting File...
Writing 1.csv.gz
Writing 2.csv.gz
Writing 3.csv.gz
Writing 4.csv.gz
Writing 5.csv.gz
Writing 6.csv.gz
Writing 7.csv.gz
Writing 8.csv.gz
Writing 9.csv.gz
Writing 10.csv.gz
--- 81.30534887313843 seconds ---
```

### S3 Bucket

https://s3.us-east-2.amazonaws.com/mm-challenge/1.csv.gz


