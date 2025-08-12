#!/usr/bin/python3
"""8-json_api module"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    param = {"q": argv[1] if len(argv) > 1 else ""}
    r = requests.post(url, data=param)
    try:
        jsonstr = r.json()
        if jsonstr:
            print(f'[{jsonstr.get("id")}] {jsonstr.get("name")}')
        else:
            print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
