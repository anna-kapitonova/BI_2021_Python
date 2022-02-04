#! /usr/bin/env python
import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="UNIX tool rm analog: remove directory entries")
parser.add_argument("-r", action='store_true',
                    help="Attempt to remove the file hierarchy rooted in each file argument")
parser.add_argument('input_names', nargs='+', help='print the file- or dirnames')
args = parser.parse_args()


def main():
    for name in args.input_names:
        if os.path.isfile(name) is True:
            os.remove(name)
        else:
            if args.r is True:
                shutil.rmtree(name)
            else:
                print("rm: "+name+": is a directory")


main()
