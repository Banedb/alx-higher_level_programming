#!/usr/bin/python3
"""3-error_code module"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as r:
            print(r.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
