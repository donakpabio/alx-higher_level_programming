#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            if len(matrix[n]) - 1 == m:
                print("{:d}".format(matrix[n][m]))
            else:
                print("{:d}".format(matrix[n][m]), end=' ')

    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("{}".format(""))


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
