#!/usr/bin/python3
for n in range(0, 10):
    for m in range(0, 10):
        if int(repr(n) + repr(m)) < int(repr(m) + repr(n)):
            if int(repr(n) + repr(m)) < 89:
                print("{:02}".format(int(repr(n) + repr(m))), end=', ')
            else:
                print("{:02}".format(int(repr(n) + repr(m))))
