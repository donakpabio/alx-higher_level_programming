#!/usr/bin/python3


def number_keys(a_dictionary):
    count = 0
    for x, y in a_dictionary.items():
        count = count + 1
    return count


if __name__ == "__main__":
    number_keys(a_dictionary)
