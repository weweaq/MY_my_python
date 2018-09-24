import requests
import re
import json


def open_url(name):
    url = 'https://s.taobao.com/search'
    payload = {
        'q': name,
        'sort': 'sale-desc'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }

    res = requests.get(url, headers=header, params=payload)

    # with open('taobao_xjy.text', 'w', encoding='utf-8') as f:  保存网页为text
    #     f.write(res.text)

    # with open('taobao_xjy.text', 'r', encoding='utf-8') as f:
    g_page_config = re.search(r'g_page_config = (.+?);\n', res.text).group(1)
    target_page_config = json.loads(g_page_config)

        # with open('page_config.text', 'w', encoding='utf-8') as file: 提取g_page_config为text
        #     file.write(g_page_config)

    return target_page_config
    # print(name + '\n')
    # print(author_name + '\n')


def get_space(level):
    return ' ' * level + '+'


def find_key(target, level):
    result = []
    target_content = target['mods']['itemlist']['data']['auctions']

    for each_item in target_content:
        data_item = dict.fromkeys(('view_price', 'item_loc', 'view_sales', 'comment_count', 'nick'))
        data_item['view_price'] = each_item['view_price']
        data_item['item_loc'] = each_item['item_loc']
        data_item['view_sales'] = each_item['view_sales']
        data_item['comment_count'] = each_item['comment_count']
        data_item['nick'] = each_item['nick']
        result.append(data_item)

    for each in result:
        print(each['view_price'])
        print(each['item_loc'])
        print(each['view_sales'])
        # print(re.search(r'\d+', each['view_sales']).group())                 正则表达式提取数据
        print('评价次数：' + each['comment_count'])
        print(each['nick'] + '\n' + '-------------------------')


    # 打印树，方便检查，查找数据

    # keys = iter(target)
    # print( type(target['mods']))
    #
    # for each in target:
    #     if type(target[each]) is not dict:
    #         print(get_space(level)+each)
    #     else:
    #         next_level = level
    #         print(get_space(next_level)+each)                             #写递归函数时一定要注意顺序，比如说print的顺序，因为这是递归
    #         next_level = level + 1
    #         find_key(target[each], next_level)


def main():
    name = input('please input the name of your goods:')
    target_page_config = open_url(name)
    find_key(target_page_config, 1)


if __name__ == '__main__':
    main()
