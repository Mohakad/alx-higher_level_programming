#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = list(map(lambda r: list(map(lambda x: x**2, r)), matrix))
    return newm
