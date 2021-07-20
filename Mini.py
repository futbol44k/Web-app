import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import googleapiclient.discovery

SORRY2 = pd.DataFrame({
        'name': ['No such anime']
    })
SORRY = pd.DataFrame({
        'character': ["There is no matching characters in data"]
    })

class FindAnime:
    def __init__(self, data: pd.DataFrame):
        self.data = data


    @staticmethod
    def from_csv_path(csv_path: str):
        return FindAnime(pd.read_csv(csv_path))


    def similar_word_in_name(self, word=''):
        if word == '':
            return self.data
        index_match_data = self.data.apply(
            lambda row: word.lower() in row['name'].lower(),
            axis=1
        )
        data_sample = self.data[index_match_data]
        if data_sample.empty:
            return data_sample
        return data_sample
    
    
    def similar_year(self, y=''):
        if y == '':
            return self.data
        index_match_data = self.data.apply(
            lambda row: y.lower() in row['year'].lower(),
            axis=1
        )
        data_sample = self.data[index_match_data]
        if data_sample.empty:
            return data_sample
        return data_sample
    
    
    def similar_tags(self, arr=''):
        if arr == '':
            return self.data
        k = list(arr.split())
        data_sample = self.data
        for tag in k:
            index_match_data = data_sample.apply(
                    lambda row: tag.lower() in row['genres'].lower(),
                    axis=1
                )
            data_sample = data_sample[index_match_data]
        if data_sample.empty:
            return data_sample
        return data_sample


    def sim_char_tags(self, name=''):
        index_match_data = self.data.apply(
                lambda row: name.lower() in row['titles with character'].lower(),
                axis=1
            )
        data_sample = self.data[index_match_data]
        if data_sample.empty:
            return SORRY
        return data_sample.sample(1)


    def find(self, y='', arr='', word=''):
        data_sample1 = self.similar_word_in_name(word)
        data_sample2 = self.similar_year(y)
        data_sample3 = self.similar_tags(arr)
        s1 = pd.merge(data_sample1, data_sample2, how='inner', on=['name'])
        s2 = pd.merge(s1, data_sample3, how='inner', on=['name'])
        if s2.empty:
            print('No such anime')
            return SORRY2
        return s2[['name', 'year', 'genres', 'url', 'description']].sample(1)


    def rand_char(self, simp, y='', arr='', word=''):
        data_sample = simp.find(y, arr, word)
        m = self.sim_char_tags(data_sample['name'].iloc(0)[0])
        #return m['character'].iloc(0)[0]
        return m, data_sample


def review(title: str):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    with open("./token.txt") as f:
            api_key = f.read()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = api_key)

    request = youtube.search().list(
        part="snippet",
        q="обзор на аниме {}".format(title)
    )
    response = request.execute()

    return response['items'][0]['id']['videoId']


simp = FindAnime.from_csv_path("./anime_db.csv")
charac = FindAnime.from_csv_path("./second_anime_db.csv")
#print(charac.rand_char(simp, '', '', ''))
#print(review(simp.find('', '', 'наруто')))