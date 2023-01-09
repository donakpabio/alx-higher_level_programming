#!/usr/bin/python3


def multiple_returns(sentence):
    size = len(sentence)
    return tuple((size, None if size == 0 else sentence[0]))


if __name__ == "__main__":
    multiple_returns(sentence)
