#!/usr/bin/python3
"""5-hbtn_header module"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
