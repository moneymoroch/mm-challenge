# mm-challenge
```
git clone https://github.com/moneymoroch/mm-challenge.git
cd mm-challenge
python3 gen.py
cat source.csv | python3 generate_stats.py
gzip -f source.csv
python3 split.py
```
