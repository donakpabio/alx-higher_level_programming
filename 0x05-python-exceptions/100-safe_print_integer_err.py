#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except Exception as err:
        print("Exception: {}".format(err))


if __name__ == "__main__":
    list_division(my_list_1, my_list_2, list_length)
