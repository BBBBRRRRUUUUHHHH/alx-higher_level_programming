#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print(f"\t- utf8 content: {body.decode('utf-8')}")
