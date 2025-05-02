#!/usr/bin/python3
"""101-nqueens: Solves the N-Queens problem using iterative backtracking."""
import sys


def nqueens(num):
    """Iteratively solves the N-Queens problem and prints each solution.

    Args:
        num (int): size of the board and number of queens
    """

    table = {}  # table of candidates
    solution = []  # viable solution to the nqueens problem
    idx = []  # idx to iterate through candidates
    line = 0  # row

    while 0 <= line < num:
        candidates = [col for col in range(num) if not any
                      (col == c or abs(line - r) == abs(col - c)
                       for r, c in solution)]  # collect column candidates
        if candidates:
            if f"row{line}" not in table:
                idx.append(0)
                table[f"row{line}"] = candidates
            else:
                idx[line] += 1
            try:
                solution.append([line, candidates[idx[line]]])
                line += 1
            except IndexError:  # Exhausted options in current line, backtrack
                table.pop(f"row{line}", None)
                idx.pop()
                if solution:
                    solution.pop()
                line -= 1
        else:  # No candidates, backtrack
            try:
                idx[line - 1] += 1
                solution[line - 1][1] = table[f"row{line - 1}"][idx[line - 1]]
            except IndexError:  # Backtrack further
                del solution[-2:]
                table.pop(f"row{line - 1}", None)
                idx.pop()
                line -= 2

        if len(solution) == num:
            print(solution)
            # Prepare for next solution
            del solution[-2:]
            table.pop(f"row{line - 1}", None)
            idx.pop()
            line -= 2


def main():
    """Parses arguments and calls nqueens."""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(num)


if __name__ == "__main__":
    main()
