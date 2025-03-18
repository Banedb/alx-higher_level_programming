#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            print((" ".join(["{}"] * len(row))).format(*row))
    else:
        print("{}".format("\n"), end="")
