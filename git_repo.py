import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# process results
response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visualizatiom
data = [{
        'type': 'bar',
        'x': repo_names,
        'y': stars,
        'marker': {
            'color': 'rgb(60, 40, 120)',
            'line': {
                'width': 1.5,
                'color': 'rgb(25, 25, 25)'
            },
        },
        'opacity': 0.6,
        }]
my_layout = {
    'title': 'Most Starred Python Projects in Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout, }
offline.plot(fig, filename='pyrepo.html')
