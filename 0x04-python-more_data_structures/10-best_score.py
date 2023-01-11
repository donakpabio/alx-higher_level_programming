#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        hv = 0
        hk = None
        counter = 0
        for x, y in a_dictionary.items():
            if counter == 0:
                hv = y
                hk = x
            else:
                hv = hv if hv > y else y
                hk = hk if hv > y else x
            counter = counter + 1
        return hk
    return None


if __name__ == "__main__":
    best_score(a_dictionary)
