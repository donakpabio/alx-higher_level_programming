#!/usr/bin/python3
import sys
import hidden_4


def add1():
    list = dir(hidden_4)
    for n in range(1, len(list)):
        if "__" not in list[n]:
            print("{}".format(list[n]))


if __name__ == "__main__":
    add1()
