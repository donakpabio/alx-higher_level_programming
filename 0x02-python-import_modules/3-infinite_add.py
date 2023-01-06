#!/usr/bin/python3
import sys


def add1():
    a = 0
    for n in range(1, len(sys.argv)):
        a = a + long(sys.argv[n])
    print("{}".format(a))


if __name__ == "__main__":
    add1()
