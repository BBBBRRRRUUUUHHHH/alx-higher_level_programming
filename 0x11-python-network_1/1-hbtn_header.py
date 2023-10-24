#!/usr/bin/python3
<<<<<<< HEAD
import.urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen.(req) as response:
    body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
=======
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(f"{x_request_id}")
>>>>>>> 9365a378051245702088e551a671ba5e1163eb60
