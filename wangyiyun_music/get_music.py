# Created by weweaq at 2018/9/20
#  < encoding = "utf-8">
import requests
import os
import re
import json
import csv
import pymongo
from bs4 import BeautifulSoup


mongo_url = 'localhost'
mongo_db = 'wangyiyun_mp4'
mongo_table = 'src_info'

client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]


def save(result):
    try:
        if db[mongo_table].insert(result):
            print('save to mongo success', result)
    except Exception:
        print("save failed", result)


def download_music(song_id, songName, albumName):
    music_url = 'https://music.163.com/song/media/outer/url?id=' + str(song_id) + '.mp3'
    res = requests.get(music_url)
    print('正在下载歌曲 ： 《%s》              ++++++++++++++++++' % songName)
    print('属于专辑 :  %s  ' % albumName)
    print('---------------------------------------------------------------------------')
    with open(songName + '.mp4', 'ab') as f:
        f.write(res.content)
        print('download  success')
    print(' ')


def get_music_info(art_id):
    song_info = []
    header = {

        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36',
        'Referer': 'https://music.163.com/song?id=208958'
    }

    url = 'https://music.163.com/artist?id=' + art_id
    res = requests.get(url, headers=header)
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
        song_info.append(dict(song_id=each['id'], song_name=each['songName'].replace('/xa0', ' '), song_albumName=each['albumName']))
        with open('list.csv', 'a', newline='') as csvfile:
            eWriter = csv.writer(csvfile)
            eWriter.writerow([each['id'], each['songName'].replace('\xa0', ' '), each['albumName']])
        download_music(each['id'], each['songName'], each['albumName'])

    return song_info


def main():
    music_id = input('please input the artist id:')
    res_sum = get_music_info(music_id)
    save(res_sum)


if __name__ == '__main__':
    main()

    #   with open('l.csv', 'a', newline='') as csvfile:
    #     eWriter = csv.writer(csvfile)
    #     eWriter.writerow([each['id'], each['songName'], each['albumName']])
    # print(dict(song_id=each['id'], song_name=each['songName'], song_albumName=each['albumName']))

    # all_info = {
    #     'song_name':info[]
    # }

    # print(info)
    # with open('res.text', 'w') as f:
    #     f.write(str(info))
    #   字典不可以直接写入文件，需要先转str

    #   print()里面可以有两个%s 吗  怎么弄
    #   答： 是当然可以的啊，注意要用括号括起来喔     print('%s   %s' % ('123', '456'))

    #   UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 17: illegal multibyte sequence
    #   上述错误的意思是，当把'utf-8'的格式转换成Unicode时， '\xa0'在电脑里的'gbk'不可以编译出来，所以解决方法是，使用
    #   字符串专属的函数, 'str'的replace（'old', 'new'）函数，将不能编译的替换掉，替换成 ' '空格也行
