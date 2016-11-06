import requests

client_id = '8e75dde9e5eb05765455'
client_secret = 'ab967317413812b3a9d52463d5ac1685'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# достаем токен
token = r.json()["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

url_prefix = "https://api.artsy.net/api/artists/"

artists = dict()
with open('dataset_24476_4.txt', 'r') as f:
    for line in f:
        url = url_prefix + line.rstrip()
        r = requests.get(url, headers=headers).json()
        artists.update({r["sortable_name"]: r["birthday"]})

sorted_artists = sorted(list(artists.keys()), key=lambda x: artists[x] + x)
[print(art) for art in sorted_artists]