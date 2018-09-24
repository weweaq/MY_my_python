import requests
import json
import re
import demjson
import pymongo
from config import *
from urllib.parse import urlencode


client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]


def save(result):
    try:
        if db[mongo_table].insert(result):
            print('save success', result)
    except Exception:
        print("save failed", result)


def get_page_index(base, keyword, offset):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'format': 'json',
        'keyword': keyword,
        'offset': offset,
    }

    params = urlencode(data)
    url = base + '?' + params
    res = requests.get(url, headers=header)
    # res = requests.post(url, headers=header, data=data)
    # print(res.text)
    res = json.loads(res.text)

    return res
    # with open('res3.text', 'w', encoding='utf-8') as f:
    #     f.write(res.text)


def get_page_url_index(res):
    if res and 'data' in res.keys():
        for each in res.get('data'):
            yield each.get('article_url')


def get_pic_adds(target_url):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    res = requests.get(target_url, headers=header)
    if re.search(r'gallery: JSON.parse\((.+?)\),\n', res.text) is not None:                            #'NoneType' object has no attribute 'group'  当research找不到时，返回的就是None group()找不到
        b = demjson.decode(re.search(r'gallery: JSON.parse\((.+?)\),\n', res.text).group(1))           #demjson 可以协助解码，本来是显示英文乱字符串的，可以显示中文，而且可以双引号
        # print(type(re.search(r'gallery: JSON.parse(.+?)\),\n', res.text).group(1)))                  #str 类型 字符串，不可以直接for
        # for each in json.loads(b):
            # for each_img_adds in each['sub_images']:
            #     print(each_img_adds)
        for each in json.loads(b)['sub_images']:
            result = {'pic_url':each['url']}
            save(result)






def main():
    base = 'http://www.toutiao.com/search_content/'
    # keyword = input('please input your keyword:')
    # pages = input('please input your pages:')
    page_adds = []

    for each_page in range(int(5)):
        res = get_page_index(base, "街拍", each_page*20)
        for each in get_page_url_index(res):
            if each is not None:                                                #type(None) == NoneType   each == None
                if len(each) == 45:
                    page_adds.append(each)


    # for each in page_adds:
    #     print(each)

    for each_adds in page_adds:
        if each_adds is not None:
            get_pic_adds(each_adds)


if __name__ == '__main__':
    main()
