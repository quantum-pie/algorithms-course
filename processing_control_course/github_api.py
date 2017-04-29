"""
 Having fun with Github API
 """

import requests, re

user_name = 'quantum-pie'
user_pwd = 'dummy'

requests.get('https://api.github.com/user', auth=(user_name, user_pwd))

url_prefix = 'https://api.github.com/repos/'
re_pattern = r'https://github.com/'

with open('awesome_pipeline_repos') as f:
 for url in f:
     owner_repo = url_prefix + re.sub(re_pattern, '',  url.rstrip())
     r = requests.get(owner_repo).json()
     def_branch = r['default_branch']
     g = 0