#!/usr/bin/python3
"""
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response headers")
