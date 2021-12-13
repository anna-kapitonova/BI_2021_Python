#! /usr/bin/env python
import sys
import argparse


def sort_tool(file):
    with open(file) as f:
        f_lines = f.read().splitlines()
        f_lines.sort()
    return('\n'.join(f_lines))


def main():
    print(sort_tool(args.file))


if not sys.stdin.isatty():
    input_file = sys.stdin.read().splitlines()
    input_file.sort()
    print('\n'.join(input_file))


# otherwise, read the given filename                                            
else:
    parser = argparse.ArgumentParser(description="UNIX tool sort analog: sort lines of text and binary files")
    parser.add_argument('file', help='print the filename')
    args = parser.parse_args()
    main()
