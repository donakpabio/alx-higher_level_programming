#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            if len(matrix[n]) - 1 == m:
                print("{}".format(matrix[n][m]))
            else:
                print("{}".format(matrix[n][m]), end=' ')


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
