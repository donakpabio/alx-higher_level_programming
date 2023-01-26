#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    try:
        for n in range(list_length):
            try:
                my_list_3.append(float(my_list_1[n]) / float(my_list_2[n]))
            except ZeroDivisionError:
                my_list_3.append(0)
                print("division by 0")
            except (TypeError, ValueError):
                my_list_3.append(0)
                print("wrong type")
    except IndexError:
        my_list_3.append(0)
        print("out of range")
    return my_list_3


if __name__ == "__main__":
    list_division(my_list_1, my_list_2, list_length)
