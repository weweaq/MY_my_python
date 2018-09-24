# Created by weweaq at 2018/8/29
#  < encoding = "utf-8">


import requests
import os
import json
import re
import urllib.parse
from bs4 import BeautifulSoup


def get_page(since, url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36',
    }
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    page_id = soup.find('div', class_='moreComent js-appBtn mt8')['data-id']

    target_url = 'https://bcy.net/circle/timeline/loadtag?' + 'since=' + str(
        since) + '&grid_type=timeline&tag_id='+str(page_id)+'&sort=hot'

    return target_url
    # with open('res.text', 'w', encoding='utf-8') as f:
    #     f.write(res.text)
    #     print('success')


def get_page_detail(target_url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36',
    }
    since = []
    id_item = []

    res = requests.get(target_url, headers=header)
    res_list = json.loads(res.text)
    # since, num 提取
    if res_list and 'data' in res_list.keys():
        for each in res_list['data']:
            since.append(each['since'])
            id_item.append(each['item_detail']['item_id'])

    return since, id_item


def get_img(data):
    # for each in data:
    img_url = 'https://bcy.net/item/detail/' + str(data[0])
    get_img_src(img_url)


def get_img_src(img_url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36',
    }
    res = requests.get(img_url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_addrs = soup.find_all('img', class_='detail_std detail_clickable')
    print('下载目标图片专栏：'+soup.title.string)
    for each in img_addrs:
        print('正在下载图片：'+each['src'])
        save_img(each['src'])

    # TypeError: 'module' object is not callable 因为没有加上方法，落掉了.get()
    # with open('res.text', 'w', encoding='utf-8') as f:
    #     f.write(res.text)
    #     print('success')


def save_img(img_url):
    img_name_data = re.search(r'item(.*)\.jpg', img_url)
    if img_name_data is not None:
        with open((img_name_data.group().split('/', 5)[-1]), 'wb') as f:
            f.write(requests.get(img_url).content)


def main():
    if not os.path.exists('cosplay'):
        os.mkdir('cosplay')
    os.chdir('cosplay')

    name = input('please input the name you want:')
    url_name = urllib.parse.quote(name)
    file_name = name.encode('utf-8').decode('utf-8', 'ignore')
    # 按照网上的教程说，windows里的编码格式都是'gbk'编码，python下的都是'utf-8'格式编码，所以要创建带汉字的文件夹应该是要将'utf-8'转换成'gbk'格式
    # 在我的实际操作过程中，将汉字重新'utf-8'编码，然后再按'utf-8'解码就又好了，真的是很神奇
    # ps:注意，字符串和字节字符串是很不同的，字符串没有decode（）方法， 如：'张俊' 与 '\u5f20\u4fca'
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    os.chdir(file_name)

    # b = demjson.decode(name)  用这个是不可以的，这个是把网址字符串变成中文，自动补全json文件，不可以将汉字变成网址字符串
    # 这里是需要使用urllib.parse.quote（）方法，将汉字重新编码，加入到字符串
    url = 'https://bcy.net/tags/name/{}'.format(url_name)
    target_url = get_page(0, url)
    data = get_page_detail(target_url)
    get_img(data[1])
    img_list = data[0]

    # https://www.cnblogs.com/PPhoebe/p/6710055.html 列表的切片
    while 1:
        for each in list(set(img_list)):
            target_url = get_page(each, url)
            data_img = get_page_detail(target_url)
            get_img(data_img[1])

        img_list = data_img[0]


if __name__ == '__main__':
    main()




# print(re.search(r'item(.*)\.jpg', a))
# <_sre.SRE_Match object; span=(37, 88), match='item/web/179qh/eb46fd30a7fe11e88b87336026092568.j>
# print(re.search(r'item(.*)\.jpg', 'item/web/179qh/eb46fd30a7fe11e88b87336026092568.jpg'))
# <_sre.SRE_Match object; span=(0, 51), match='item/web/179qh/eb46fd30a7fe11e88b87336026092568.j>
# print(re.search(r'item(.*)\.jpg', 'item/web/179qh/eb46fd30a7fe11e88b87336026092568.j'))
# None
# print(re.search(r'web(.*)\.jpg', 'item/web/179qh/eb46fd30a7fe11e88b87336026092568.j'))
# None
# print(re.search(r'web(.*)\.jpg', 'item/web/179qh/eb46fd30a7fe11e88b87336026092568.jpg'))
# <_sre.SRE_Match object; span=(5, 51), match='web/179qh/eb46fd30a7fe11e88b87336026092568.jpg'>