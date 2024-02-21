#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            decoded_response = response.read().decode('utf-8')
            print(decoded_response)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
