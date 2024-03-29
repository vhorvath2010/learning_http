# File to generate statistics on the commits to this Git repo
import requests
import json

# Get repo
repo = input("Enter the repo in the format %user%/%repo%: ")

# Get JSON data for all commits
api = "https://api.github.com"
res = requests.get(api + "/repos/" + repo + "/commits")
json_data = res.json()

# Create map of commit authors to # of commits
num_commits = {}
for commit in json_data:
    author = commit['commit']['author']['email']
    num_commits[author] = num_commits.get(author, 0) + 1

# Serialize to JSON response
json_response = json.dumps(num_commits, indent=2)
# Pseudo post content to API
# post_res = requests.post("post-url", json=json_response)
print("Here are the commits per user of", repo)
print(json_response)

# Find info about all commits (practice with headers/params)
print("Finding all of my commits this month")
commit_data_res = requests.get(api + "/search/commits",
                               headers={'accept': 'application/vnd.github+json'},
                               params={'q': 'author:vhorvath2010 committer-date:>=2022-07-29'})
commit_data_json = commit_data_res.json()
print(commit_data_json)
