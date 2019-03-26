# mm-challenge
```
git clone https://github.com/moneymoroch/mm-challenge.git
cd mm-challenge
python3 gen.py
cat source.csv | python3 generate_stats.py
gzip -f source.csv
python3 split.py
```

##[+] How many rows did you generate? Why?

```
23599999 rows
The program gen.py writes rows dynamically based on the current file size until the desired size is reached. Thus
the amount of rows will almost always be different each run since the contents of the rows are random. 


```

