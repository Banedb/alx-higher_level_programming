#!/usr/bin/python3
"""10-my_github module"""
if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    r = requests.get(url, auth=auth)
    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print("None")
