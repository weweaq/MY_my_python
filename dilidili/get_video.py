# Created by weweaq at 2018/9/14
#  < encoding = "utf-8">


import requests


def get_url(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',

        'Referer': 'https://music.163.com/song?id=208958'
    }
    video_url = 'http://110.80.136.9:2100/share/2O3oL3MttVldRLc3'
    res = requests.get(video_url, headers=header)

    with open('bb.mp4', 'ab') as f:
        f.write(res.content)


def main():
    url = 'www.dilidili.wang'
    get_url(url)


if __name__ == '_main__':
    main()