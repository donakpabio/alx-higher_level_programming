#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True)
    for n in range(len(my_list)):
        print("{:d}".format(int(my_list[n])))


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
