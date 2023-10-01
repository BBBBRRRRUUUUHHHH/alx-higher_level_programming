#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
import sys
url = requests.get(sys.argv[1])
if __name__ == '__main__':
    if url.status_code >= 400:
        print("Error code:", url.status_code)
