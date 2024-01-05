#!/usr/bin/python3
""" 101-nqueens
This module contains functions for solving the N queens problem

Functions:
    check_spot(board, r, c):
    init_board(n=4):
    solve(board, row):
    fix(board):
    nqueens(n=4):
    main():

"""


from sys import argv


def check_spot(board, r, c):
    """Checks spots for the board.

    Args:
        board (list): A board to check.
        r (int): Row.
        c (int): Column.

    Return:
        0: On success.
        1: On failure.
    """

    n = len(board) - 1

    if board[r][c]:
        return 0

    for row in range(r):
        if board[row][c]:
            return 0

    i = r
    j = c
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j]:
            return 0

    i = r
    j = c
    while i > 0 and j < n:
        i -= 1
        j += 1
        if board[i][j]:
            return 0

    return 1


def init_board(n=4):
    """Initializes the board.

    Args:
        n (int, optional): The number of queens. Defaults to 4.

    Returns:
        board: The initialized board.
    """

    board = []
    for _ in range(n):
        board.append([0 for _ in range(n)])
    return board


def solve(board, r):
    """Solves a row in the board.

    Args:
        board (list): The board.
        row (int): The row to solve.

    Returns:
        board: The solved board.
        None: On failure.
    """

    for c in range(len(board)):
        if check_spot(board, r, c):
            board[r][c] = 1

            if r == len(board) - 1:
                print(fix(board))
                board[r][c] = 0
                continue
            elif solve(board, r + 1):
                return board
            else:
                board[r][c] = 0
    return


def fix(board):
    """Gets the solution.

    Args:
        board (list): The board to apply the solution.

    Returns:
        The solution.
    """

    solution = []

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:
                solution.append([r, c])
    return solution


def nqueens(n=4):
    """Solves row by row in each column.

    Args:
        n (int, optional): The number of queens. Defaults to 4.
    """

    for col in range(n):
        board = init_board(n)
        board[0][col] = 1
        solve(board, 1)


def main():
    """Validates arguments and starts solving.
    """

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(n)


if __name__ == "__main__":
    main()
