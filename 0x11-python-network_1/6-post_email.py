#!/usr/bin/python3
"""6-post_email module"""
if __name__ == "__main__":
    from sys import argv
    import requests

    data = {"email": argv[2]}
    r = requests.post(argv[1], data=data)
    print(r.text)
