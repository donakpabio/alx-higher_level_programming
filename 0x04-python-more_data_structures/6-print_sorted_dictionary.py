#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    dlist = list(a_dictionary)
    dlist.sort()
    for n in range(len(dlist)):
        print("{}: {}".format(dlist[n], a_dictionary[dlist[n]]))


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
