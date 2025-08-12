#!/usr/bin/python3
"""0-hbtn_status module"""
if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen("https://alx-intranet.hbtn.io/status") as r:
        content = r.read()
        print("Body response:")
        print(f"\t - type: {type(content)}")
        print(f"\t - content: {content}")
        print(f'\t - utf8 content: {content.decode("utf-8")}')
