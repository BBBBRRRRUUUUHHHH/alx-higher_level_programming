#!/usr/bin/python3
<<<<<<< HEAD
# Write a Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print(f"\t- utf8 content: {body.decode('utf-8')}")
=======
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    content_utf8 = content.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content_utf8)
>>>>>>> 9365a378051245702088e551a671ba5e1163eb60
