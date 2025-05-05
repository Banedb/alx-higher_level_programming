#!/usr/bin/python3
"""101-stats module: Reads stdin line by line, computes metrics
and prints after every 10 lines."""


import sys

file_size = 0
status_table = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


def print_stats():
    """Prints stats"""
    print(f"File size: {file_size}")
    for k, v in sorted(status_table.items()):
        if v > 0:
            print(f"{k}: {v}")


try:
    for count, line in enumerate(sys.stdin, start=1):
        pieces = line.split()
        try:
            file_size += int(pieces[-1])
            if pieces[-2] in status_table:
                status_table[pieces[-2]] += 1
        except (IndexError, ValueError):
            pass

        if count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
