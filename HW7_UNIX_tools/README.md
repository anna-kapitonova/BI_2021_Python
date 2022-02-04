## HW7 - Python analogs of UNIX tools

There are five tools:
- wc with options -l -w- c
- ls with option -a
- sort (without options)
- rm with option -r
- cat without options

#### Instructions:
- download the files *.py
- make the scripts executable in your command line via following command
```
chmod +x script.py
```
- launch script.py with avalaible options and required arguments (use -h for help)
```
./script.py [...]
```

You can also use all these programms in pipes (also with UNIX utilities) like that:
```
./ls.py | ./wc.py -l 
cat *.tsv | sort | ./wc.py -w
```
