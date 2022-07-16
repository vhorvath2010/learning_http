# File to generate statistics on the commits to this Git repo
import requests
import json

# Get JSON data for all commits
api = "https://api.github.com"
res = requests.get(api + "/repos/vhorvath2010/learning_http/commits")
json_data = res.json()

# Create map of commit authors to # of commits
num_commits = {}
for commit in json_data:
    author = commit['commit']['author']['email']
    num_commits[author] = num_commits.get(author, 0) + 1

# Serialize to JSON response
json_response = json.dumps(num_commits, indent=2)
# Pseudo post content to API
# post_res = requests.post(api + "/repos/vhorvath2010/learning_http/commits", json=json_response)
print(json_response)
