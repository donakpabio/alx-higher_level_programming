#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    rem = []
    for k, v in a_dictionary.items():
        if v == value:
            rem.append(k)
    for n in range(len(rem)):
        del a_dictionary[rem[n]]
    return a_dictionary


if __name__ == "__main__":
    complex_delete(a_dictionary, value)
