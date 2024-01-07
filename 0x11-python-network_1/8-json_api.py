#!/usr/bin/python3
"""
takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
