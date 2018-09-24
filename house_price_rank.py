from bs4 import BeautifulSoup
import re
import os
import requests


def open_url(url):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    res = requests.get(url, headers=header)

    return res


def get_url(res):

    data = []

    soup = BeautifulSoup(res.text, 'html.parser')

    contents = soup.find('div', class_='fjlist-wrap clearfix')
    content = contents.find_all('a')

    content = iter(content)

    # print(re.search(r'年(.+)<', str(content[1])).group(1))
    for each in content:
        if re.search(r'年(.+)<', str(each)) is None:
            print(re.search(r'年(.+)<', str(next(content))).group(1))
        else:
            print(re.search(r'年(.+)<', str(each)).group(1))


      #   data.append(
      #
      # )







def main():

    if (os.path.exists('house_price_rank') == False):
        os.mkdir('house_price_rank')
    os.chdir('house_price_rank')

    url = 'https://www.anjuke.com/fangjia/quanguo2017/'
    res = open_url(url)

    # with open('price_rank', 'w', encoding='utf-8') as f:
    #     f.write(res.text)

    get_url(res)


if __name__ == '__main__':
    main()

 #正则表达式中不可以加括号！ 切记
 #re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d)", '200.123.10.250')
 #re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d", '200.123.10.250') |（或） 自己加括号
