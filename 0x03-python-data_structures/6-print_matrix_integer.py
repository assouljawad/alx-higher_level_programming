#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print("")
    for raw in matrix:
        for i in range(0, len(raw)):
            if i != (len(raw) - 1):
                print('{:d}'.format(raw[i]), end=" ")
            else:
                print('{:d}'.format(raw[i]))
