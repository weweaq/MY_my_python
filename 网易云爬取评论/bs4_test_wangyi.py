import requests
import json


def open_url():
    url = input('please input your url: ')

    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36'}

    res = requests.get(url, headers=header)

    return res


def get_comments():
    url = input('please input your url: ')

    name_id = url.split('=')[1]

    header = {

        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Mobile Safari/537.36',
        'Referer': 'https://music.163.com/song?id=208958'
    }

    data_num = {
        'encSecKey':'97644d6419e403af285c6b1ab1560edd7acaaa5f29a163301e35f850e7dac4d039aec6'
                    'e3f45590a26701fd9913ba06cfe09e8c33765c76a7896b3e2ad548ccf544ac7331a3ed'
                    'a2783591ef6f32dbf1ffc6929ee8e1817aeda216cef634151c59a4f5361b074cb914c84'
                    'dc2597eee70f6fa03905ea95c9690e0756a9921fec5e3',
        'params':'3c'
                 '/FOeTeuQ8LoDegzbbdys7zhUuBYAon8p9apC6AjQHXlzejeqoDQCu1tGufNgXoWkxQTYiMMmLmMT7lPIbekXbycd9Xbdk4A5Wz'
                 '/PLLudS4uLUQBgLI93qv69cJZwpaKCRwt19cSdysxpUAj4ytMB7ViBEyYgyetxtFiIrMyHef3u8pEBlB3TGDFAhG1xr9fpr'
                 '+059bABWfkRJOhX6sv/dxdiRX119BkT3m0G0YCRs='}

    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}'.format(name_id)

    res = requests.post(target_url, headers=header, data=data_num)
    comment_json = json.loads(res.text)
    # print(type(res.text))  # 这边的res.text虽然打开显示的格式是字典类型，由大括号括起来，print()出来也是有大括号括起来，并没有像
    # print(res.text)        #字符串格式的" "包起来，可是仍然是字符串类型，需要json.loads()将字符串转化成字典类型
    # print(comment_json)
    hot_comment = comment_json['hotComments']
    # print(hot_comment)

    with open('res1.text', 'w', encoding='utf-8') as f:
        for each in hot_comment:
            f.write(each['user']['nickname']+':\n\n')
            f.write(each['content']+'\n')
            f.write('--------------------------------\n')


def main():

    res = get_comments()


#    with open ('data.text', 'w', encoding='utf-8') as f:
#        f.write(res.text)

if __name__ == '__main__':
    main()
