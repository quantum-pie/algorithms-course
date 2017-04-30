"""
 Having fun with Github API
 """

import requests
import re

token = '89554a1687f36aaf5d1708a5a89cd419261a6630'

url_prefix = 'https://api.github.com/repos/'    # API url prefix
re_pattern = r'https://github.com/'             # basic repo URL prefix to replace with API url

total_count = 0                                 # number of commits in repos

with open('awesome_pipeline_repos') as f:       # open file with repos URLs
    for url in f:
        print(url)

        owner_repo = url_prefix + re.sub(re_pattern, '',  url.rstrip())             # repo API url
        repo = requests.get(owner_repo, params={'access_token': token}).json()      # get repo

        def_branch = repo['default_branch']                                         # extract default branch

        # get default branch
        branch = requests.get(owner_repo + '/branches/' + def_branch, params={'access_token': token}).json()

        last_sha = branch['commit']['sha']      # SHA of last commit in default branch

        # commits query parameters
        commits_q_params = {
            'sha': last_sha,
            'access_token': token,
            'since': '2015-12-31T23:59:59Z',
            'until': '2017-01-01T00:00:00Z'
        }
        commits = requests.get(owner_repo + '/commits', params=commits_q_params)    # get commits

        # enumerate commits
        if 'last' in commits.links.keys():                                      # if there are multiple results pages
            pages_pattern = r'.*page=([0-9]+)'
            last_page_url = commits.links['last']['url']                        # get last page URL
            pages_num = int(re.search(pages_pattern, last_page_url).group(1))   # get last page number
            total_count += (pages_num - 1) * 30                                 # number of commits on full pages
            commits = requests.get(last_page_url)                               # get last page

        total_count += len(commits.json())                                      # number of commits on last page

print(total_count)
