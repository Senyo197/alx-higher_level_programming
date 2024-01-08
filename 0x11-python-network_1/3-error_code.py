#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            info = response.read()
            print(info.decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
