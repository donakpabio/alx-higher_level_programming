#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: [n**2 for n in x], matrix))
