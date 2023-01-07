#!/usr/bin/python3


def no_c(my_string):
    text = ""
    for n in range(len(my_string)):
        if my_string[n] not in "cC":
            text = text + my_string[n]
    return text


if __name__ == "__main__":
    no_c(my_string)
