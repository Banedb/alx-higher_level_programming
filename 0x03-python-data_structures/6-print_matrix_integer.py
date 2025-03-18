#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            braces = " ".join(["{}"] * len(row))
            print(braces.format(*row))
    else:
        print("{}".format("\n"), end="")
