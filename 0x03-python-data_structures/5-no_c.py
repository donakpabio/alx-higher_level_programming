#!/usr/bin/python3


def no_c(my_string):
    last = len(my_string) - 1
    for n in range(len(my_string)):
        if my_string[n] not in "cC":
            print("{}".format(my_string[n]), end='\n' if n == last else '')


if __name__ == "__main__":
    no_c(my_string)
