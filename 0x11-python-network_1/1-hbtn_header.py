#!/usr/bin/python3
"""1-hbtn_header module"""
if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as r:
        print(r.info().get("X-Request-Id"))
