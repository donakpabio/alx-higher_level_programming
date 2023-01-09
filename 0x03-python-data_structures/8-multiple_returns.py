#!/usr/bin/python3


def multiple_returns(sentence):
    l = len(sentence)
    return tuple((l, None if l == 0 else sentence[0]))


if __name__ == "__main__":
    multiple_returns(sentence)
