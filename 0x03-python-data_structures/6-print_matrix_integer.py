#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            if len(matrix[n]) - 1 == m:
                print("{:d}".format(matrix[n][m]))
            else:
                print("{:d}".format(matrix[n][m]), end=' ')

    if len(matrix) == 0 or matrix is None:
        print("{}".format(""))


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
