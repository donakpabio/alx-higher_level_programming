#!/usr/bin/python3
def islower(c):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for n in range(len(c)):
        if c[n] not in alpha:
            return False
    return True
