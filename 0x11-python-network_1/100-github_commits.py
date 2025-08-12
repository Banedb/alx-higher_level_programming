#!/usr/bin/python3
"""10-my_github module"""
if __name__ == "__main__":
    from sys import argv
    import requests

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)
    if r.status_code == 200:
        for commit in r.json()[:10]:
            author = commit.get("commit").get("author").get("name")
            print(f'{commit.get("sha")}: {author}')
    else:
        print("None")
