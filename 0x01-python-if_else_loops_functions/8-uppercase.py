#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    alpha1 = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for n in range(len(str)):
        if islower(str[n]):
            print("{}".format(alpha2[alpha1.rfind(str[n])]), end = ('\n' if (n == (len(str) - 1)) else ''))
        else:
            print("{}".format(str[n]),  end = ('\n' if (n == (len(str) - 1)) else ''))
