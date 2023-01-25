#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for n in range(x):
        try:
            print("{:d}".format(int(my_list[n])), end="")
            counter = counter + 1
        except (TypeError, ValueError):
            pass
    print("")
    return counter


if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
