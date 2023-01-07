#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    s = len(my_list)
    for n in range(s):
        print("{}".format(my_list[s - n - 1]))


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
