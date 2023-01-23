#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end='')
        except IndexError:
            print("")
            return n
    print("")
    return n + 1


if __name__ == "__main__":
    safe_print_list(my_list=[], x=0)
