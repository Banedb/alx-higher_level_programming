#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for i in (argv[1:]):
        result += int(i)
    print(f"{result}")
