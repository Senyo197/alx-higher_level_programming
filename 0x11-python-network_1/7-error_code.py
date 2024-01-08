#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the
URL and displays the body of the response using the requests module
"""

if __name__ == '__main__':
    import requests
    import sys
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
