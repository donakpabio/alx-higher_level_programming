#!/usr/bin/python3
alpha = "abcdefghijklmnopqrstuvwxyz"
for n in range(26):
    if alpha[n] not in "qe":
        print("{al}".format(al=alpha[n]), end="")
