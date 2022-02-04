#! /usr/bin/env python
import os
import argparse

parser = argparse.ArgumentParser(description="UNIX tool ls analog: list directory contents")
parser.add_argument("-a", action='store_true',
                    help="Include directory entries whose names begin with a dot (.)")
parser.add_argument('input_dirs', nargs='*', default=['./'], help='print the dirnames')
args = parser.parse_args()


def ls(dirname):
    all_list, others = list(), list()
    for name in os.listdir(dirname):
        if name.startswith("."):
            all_list.append(name)
        else:
            others.append(name)
    if args.a is True:
        all_list.sort()
        print(".", "..", sep="\n")
        print("\n".join(all_list))
    others.sort()
    print("\n".join(others))


def main():
    for dirname in args.input_dirs:
        if len(args.input_dirs) != 1:
            print(dirname+":")
        ls(dirname)


main()
