import requests
import json


git_starred_py_apirequrl = 'https://api.github.com/search/repositories?q=language:python&sort=s'

v3_header = {'Accept': 'application/vnd.github.v3+json'}

# request api
apireq = requests.get(git_starred_py_apirequrl, headers=v3_header)

print(f"Status Code: {apireq.status_code}")

# retrieve info from json
git_starred_py_dict = apireq.json()

print(f"Total Repositories: {git_starred_py_dict['total_count']}")

# process results
repo_dicts = git_starred_py_dict['items']
repo_dict = repo_dicts[0]

print(f"Repositories Returned: {len(repo_dicts)}")
print(f"Keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
