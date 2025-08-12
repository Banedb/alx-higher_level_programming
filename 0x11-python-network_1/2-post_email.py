#!/usr/bin/python3
"""2-post_email module"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode

    data = urlencode({"email": argv[2]}).encode()
    with urlopen(argv[1], data=data) as r:
        print(r.read().decode("utf-8"))
