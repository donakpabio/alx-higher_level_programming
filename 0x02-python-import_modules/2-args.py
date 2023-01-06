#!/usr/bin/python3
import sys


def add1():
    args = len(sys.argv) - 1
    dot = '.' if args == 0 else ':'
    plural = '' if args == 1 else 's'
    print("{} argument{}{}".format(args, plural, dot))
    for n in range(1, len(sys.argv)):
        print("{}: {}".format(n, sys.argv[n]))


if __name__ == "__main__":
    add1()
