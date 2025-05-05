#!/usr/bin/python3
"""101-stats module: Reads stdin line by line, computes metrics
and prints after every 10 lines."""


import sys

total = 0
status_table = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


def print_stats():
    """Prints stats"""
    print(f"File size: {total}")
    for i in sorted(status_table):
        if status_table[i] > 0:
            print(f"{i}: {status_table[i]}")


try:
    for count, line in enumerate(sys.stdin, start=1):
        my_list = line.split()
        total += int(my_list[-1])
        status_table[my_list[-2]] += 1

        if count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
