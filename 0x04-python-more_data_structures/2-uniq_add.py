#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_list.sort()
    t = 0
    for n in range(len(my_list)):
        if n == 0:
            t = my_list[n]
        else:
            if my_list[n] != my_list[n - 1]:
                t = t + my_list[n]
    return t


if __name__ == "__main__":
    uniq_add(my_list=[])
