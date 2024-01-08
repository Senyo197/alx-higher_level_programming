#!/usr/bin/python3

"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    info = (username, token)
    res = requests.get(url, auth=info)
    try:
        print(res.json().get('id'))
    except Exception:
        print('None')
