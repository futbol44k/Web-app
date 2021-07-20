import requests
from bs4 import BeautifulSoup
import pandas as pd


anime_names = []
anime_genres = []
anime_urls = []
anime_descr = []
anime_years = []
MAX_NUM_PAGES = 56
GOOD_REQUEST = 200


for page in range(MAX_NUM_PAGES):
    url = f'https://animestars.org/aniserials/video/page/{page}/'
    response = requests.get(url)
    if response.status_code != GOOD_REQUEST:
        break
    soup = BeautifulSoup(response.content, 'html.parser')
    gens = soup.find_all('div', "short-text")
    for gen in gens:
        name = gen.a.text
        url = gen.a["href"]
        hell = list(gen.div.text.split(","))
        year = hell[0]
        genres = hell[1:]
        anime_names.append(name)
        anime_genres.append(genres)
        anime_urls.append(url)
        anime_years.append(year)
    descriptions = soup.find_all('div', "short-d")
    for desc in descriptions:
        des = desc.text
        anime_descr.append(des)


df = pd.DataFrame({
    'name': anime_names,
    'genres': anime_genres,
    'year': anime_years,
    'url': anime_urls,
    'description': anime_descr
})
df.drop_duplicates(subset=['description'], inplace=True)
df.drop_duplicates(subset=['name'], inplace=True)
df.drop_duplicates(subset=['url'], inplace=True)
df.to_csv("anime_db.csv", encoding='utf-8', index=False)
#df = pd.read_csv('anime_db.csv')
#print(df)