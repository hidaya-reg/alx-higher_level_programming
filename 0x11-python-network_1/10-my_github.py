#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(user, pwd)

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
