#!/usr/bin/python3
for n in range(26):
    if n % 2 == 0:
        print("{}".format(chr(97 + 25 - n)), end='')
    else:
        print("{}".format(chr(65 + 25 - n)), end='')
