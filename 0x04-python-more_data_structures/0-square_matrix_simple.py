#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_new = []
    row_new = []

    for row in matrix:
        for item in row:
            row_new.append(item * item)
        matrix_new.append(row_new)
        row_new = []
    return (matrix_new)
