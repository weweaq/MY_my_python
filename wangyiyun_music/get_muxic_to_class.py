# Created by weweaq at 2018/9/24
#  < encoding = "utf-8">
import requests
import os
import re
import json
import csv
import pymongo
from config import *
from bs4 import BeautifulSoup


class GETMUSICINFO(object):
    def __init__(self, art_id):
        self.url = 'https://music.163.com/artist?id=' + art_id
        self.song_info = []
        self.song_msg = []

        self.header = {

            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Mobile Safari/537.36',
            'Referer': 'https://music.163.com/song?id=208958'
        }

    def get_msg(self):
        res = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(res.text, 'html.parser')
        music_info = soup.find_all('script')
        info = json.loads(re.search(r'= (.+);', str(music_info[1])).group(1))

        music_dir = soup.find('title').text
        if not os.path.exists(music_dir):
            os.mkdir(music_dir)
        os.chdir(music_dir)
        if os.path.isfile("list.csv"):
            os.remove('list.csv')
        for each in info['Artist']['songs']:
            self.song_info.append(dict(song_id=each['id'], song_name=each['songName'].replace('/xa0', ' '),
                                  song_albumName=each['albumName']))
            with open('list.csv', 'a', newline='') as csvfile:
                eerier = csv.writer(csvfile)
                eerier.writerow([each['id'], each['songName'].replace('\xa0', ' '), each['albumName']])
            self.song_msg.append(each['id'], each['songName'], each['albumName'])

class DOWNLOAD(object):
    def __init__(self, mongo_url, mongo_db):
        client = pymongo.MongoClient(mongo_url)
        db = client[mongo_db]

    def save(self):
        try:
            if db[mongo_table].insert(result):
                print('save to mongo success', result)
        except Exception:
            print("save failed", result)

def main():


if __name__ == '__main__':
    main()