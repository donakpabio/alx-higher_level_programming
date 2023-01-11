#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for n in range(len(matrix)):
        row = []
        for m in range(len(matrix[n])):
            v = matrix[n][m]
            row.append(v * v)
        new_matrix.append(row)
    return new_matrix


if __name__ == "__main__":
    square_matrix_simple(matrix=[])
