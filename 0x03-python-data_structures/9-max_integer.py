#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = 0
    for n in range(len(my_list)):
        if n == 0:
            max = my_list[n]
        max = my_list[n] if int(my_list[n]) > max else max
    return max


if __name__ == "__main__":
    max_integer(my_list=[])
