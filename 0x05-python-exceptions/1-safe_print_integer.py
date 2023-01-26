#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except Exception:
        return False


if __name__ == "__main__":
    safe_print_integer(value)
