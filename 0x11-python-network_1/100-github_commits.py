#!/usr/bin/python3
"""
 script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            commits = response.json()[:10]  # Fetch the 10 most recent commits
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error fetching data. Please check the repository and owner\
                    names.")
    except requests.RequestException:
        print("Error: Unable to connect to the GitHub API.")
