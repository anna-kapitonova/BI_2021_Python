## HW7 - Python analogs of UNIX tools

#### Instructions:
- download the files 
- make the scripts executable in your command line via following command
```
chmod +x script.py
```
- launch script.py 
```
./script.py [...]
```

You can also use all these programmes in pipes (also with UNIX utilities) like that:
```
./ls.py | ./grep.py fastq | ./wc.py -l 
cat *.tsv | sort | ./uniq.py | ./wc.py -l
```
