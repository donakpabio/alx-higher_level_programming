#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        if key in a_dictionary:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    update_dictionary(a_dictionary, key, value)
