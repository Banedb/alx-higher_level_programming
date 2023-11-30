#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print(f"1: {argv[1]}")
    elif argc > 1:
        print(f"{argc} arguments:")
        for count, arg in enumerate(argv[1:], start=1):
            print(f"{count}: {arg}")
