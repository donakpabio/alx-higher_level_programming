#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        a = 0
        b = 0
        for n in range(len(my_list)):
            a = a + my_list[n][0] * my_list[n][1]
            b = b + my_list[n][1]
        return a/b
    return 0


if __name__ == "__main__":
    weight_average(my_list=[])
