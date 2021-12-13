#! /usr/bin/env python
import sys
import argparse

if not sys.stdin.isatty():
    print(sys.stdin.read(), end="")

else:
    parser = argparse.ArgumentParser(description="UNIX tool cat analog: print files")
    parser.add_argument('files', nargs='+', help='print the filenames')
    args = parser.parse_args()
    for file in args.files:
        with open(file) as f:
            print(f.read(), end="")