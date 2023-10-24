#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url = sys.argv[1]) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

