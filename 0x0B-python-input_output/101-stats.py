#!/usr/bin/python3
"""101-stats module: Reads stdin line by line, computes metrics
and prints after every 10 lines."""


import sys

total = 0
status_table = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
status = set()


def print_stats():
    """Prints stats"""
    print(f"File size: {total}")
    for i in sorted(status):
        print(f"{i}: {status_table[i]}")


try:
    for count, line in enumerate(sys.stdin, start=1):
        my_list = line.split()
        total += int(my_list[-1])

        code = my_list[-2]
        status_table[code] += 1
        status.add(code)

        if count % 10 == 0:
            print_stats()
            status.clear()
except KeyboardInterrupt:
    print_stats()
    raise
