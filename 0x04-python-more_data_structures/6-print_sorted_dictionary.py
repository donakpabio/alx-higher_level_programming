#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary)
    for x, y in a_dictionary.items():
        print("{}: {}".format(x, y))


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
