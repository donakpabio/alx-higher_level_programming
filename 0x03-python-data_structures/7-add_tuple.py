#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    l1 = [0, 0]
    l2 = [0, 0]
    for n in range(min(len(tuple_a), 2)):
        l1[n] = int(tuple_a[n])
    for n in range(min(len(tuple_b), 2)):
        l2[n] = int(tuple_b[n])

    return tuple((l1[0] + l2[0], l1[1] + l2[1]))


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
