# Find references in given html and check if they provide 404 error

import requests
import re

pattern = r'^.*<a .*href="(.*)".*>.*</a>.*$'
html_link = input()

res = requests.get(html_link)
refs_count = 0
for line in res.text.splitlines():
    match = re.search(pattern, line)
    if match:
        res = requests.get(match.group(1))
        if res.status_code == 404:
            refs_count += 1

print(refs_count)

