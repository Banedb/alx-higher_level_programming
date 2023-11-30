#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: {}".format(argv[2]))
    elif argc > 1:
        print("{} arguments:".format(argc))
        for count, arg in enumerate(argv[1:], start=1):
              print("{}: {}".format(count, arg))
