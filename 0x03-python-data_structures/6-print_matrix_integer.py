#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for index, i in enumerate(row):
                if index == len(row) - 1:
                    print("{:d}".format(i))
                else:
                    print("{:d}".format(i), end=' ')
    else:
        print("{}".format("\n"), end="")
