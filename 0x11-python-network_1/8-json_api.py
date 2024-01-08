#!/usr/bin/python3

"""
POST request to http://0.0.0.0:5000/search_user
"""

if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    try:
        ar = sys.argv[1]
    except IndexError:
        ar = ""

    data = {"q": ar}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()

        result = response.json()

        if result:
            print("[{}] {}".format(result.get('id', 'No ID'),
                  result.get('name', 'No Name')))
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
    except ValueError:
        print("Not a valid JSON")
