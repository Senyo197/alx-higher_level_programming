#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the requests module
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
