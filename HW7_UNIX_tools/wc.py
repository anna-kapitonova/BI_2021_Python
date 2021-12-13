#! /usr/bin/env python

import sys
import os
import argparse

parser = argparse.ArgumentParser(description="UNIX tool wc analog: word, line and byte count")
parser.add_argument("-c", action='store_true',
                    help="The number of bytes in each input file is written to the standard output")
parser.add_argument("-l", action='store_true',
                    help="The number of lines in each input file is written to the standard output")
parser.add_argument("-w", action='store_true',
                    help="The number of words in each input file is written to the standard output")
args, unknown = parser.parse_known_args()


# count number of bytes
def c_bytes(file):
    n_bytes = os.path.getsize(file)
    return n_bytes


# count number of lines
def c_lines(file):
    with open(file) as f:
        n_lines = len(f.readlines())
    return n_lines


# count number of words
def c_words(file):
    with open(file) as f:
        n_words = len(f.read().split())
    return n_words


def main():
    total_bytes = 0
    total_lines = 0
    total_words = 0

    if args.c is True:
        for file in files:
            print(c_bytes(file), file)
            total_bytes += c_bytes(file)
        if len(files) != 1:
            print(total_bytes, "total")
    elif args.l is True:
        for file in files:
            print(c_lines(file), file)
            total_lines += c_lines(file)
        if len(files) != 1:
            print(total_lines, "total")
    elif args.w is True:
        for file in files:
            print(c_words(file), file)
            total_words += c_words(file)
        if len(files) != 1:
            print(total_words, "total")


# use stdin if it's full
if not sys.stdin.isatty():
    input_file = sys.stdin
    if args.c is True:
        print(len(input_file.read().encode('utf-8')))
    elif args.l is True:
        print(len(input_file.readlines()))
    elif args.w is True:
        print(len(input_file.read().split()))


# otherwise, read the given filename
else:
    parser.add_argument('files', nargs='+', help='print the filenames')
    args, unknown = parser.parse_known_args()
    files = args.files
    main()
