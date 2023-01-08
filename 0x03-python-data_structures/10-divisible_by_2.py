#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for n in range(len(my_list)):
        new_list.append(my_list[n] % 2 == 0)
    return new_list


if __name__ == "__main__":
    divisible_by_2(my_list=[])
