#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for idx, j in enumerate(matrix[i]):
            if idx + 1 != len(matrix[i]):
                print("{:d} ".format(j), end='')
            else:
                print("{:d}".format(j))
    if matrix == [[]]:
        print()
