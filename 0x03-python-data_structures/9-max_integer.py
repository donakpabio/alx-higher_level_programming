#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = 0
    for n in range(len(my_list)):
        max = my_list[n] if my_list[n] > max else max
    return max


if __name__ == "__main__":
    max_integer(my_list=[])
