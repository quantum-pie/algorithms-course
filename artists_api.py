"""
Having fun with Artsy API
"""
import requests

# no secret ;)
client_id = '8e75dde9e5eb05765455'
client_secret = 'ab967317413812b3a9d52463d5ac1685'

# request token
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# extract token
token = r.json()["token"]

# create header
headers = {"X-Xapp-Token": token}

url_prefix = "https://api.artsy.net/api/artists/"

artists = dict()

# dataset is some unknown list of artists initials
with open('dataset_24476_4.txt', 'r') as f:
    for line in f:
        url = url_prefix + line.rstrip()
        r = requests.get(url, headers=headers).json()
        artists.update({r["sortable_name"]: r["birthday"]})

# sorting artist at first by birthday and then by names if necessary
# sorry I did not know about python tuples sorting method ;)
sorted_artists = sorted(list(artists.keys()), key=lambda x: artists[x] + x)
[print(art) for art in sorted_artists]
