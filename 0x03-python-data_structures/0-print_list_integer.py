#!/usr/bin/python3


def print_list_integer(my_list=[]):
    for n in range(len(my_list)):
        print("{}".format(my_list[n]))


if __name__ == "__main__":
    print_list_integer(my_list=[])
