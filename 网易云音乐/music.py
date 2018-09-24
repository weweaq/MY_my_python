# Created by weweaq at 2018/8/27
#  < encoding = "utf-8">
import requests


def get_url(url):

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',

        'Referer': 'https://music.163.com/song?id=208958'
    }
    data = {
        'encSecKey':'07626011d238d705d4ba9949480232781808d8ee803d5173497bf9346dd04b13b9fd7f8010de75dda8'
                    'e69e6a629fe1cf154fd9c8eb802d6c68a5500164ff8f14fba8d7f7d3d5591f5efde89179d323be0850b'
                    '7f135e470b3e260f50b85029cb1d2ff8eada2f6671a21ca33e392af8265596133e37b27a97a1d86e9133db924df',

        'params':'PUQVOHSs4n+hPtAO7WOUfdRRP4s1c8EJEKVQWnk3BQZ+LAHXg4tBPHl2Lw7EN85T0PxBA7tVJGXRGRw8dps+s/Lg45ZOy' \
                 'xehTo+HukUsCUoUUlz1z30aTa1bUofv2KSmA9M4v9qaTiHdA1vUvRuWztiB8Sj2WaYv+GQpDDENno6N/umBU4mJgFsJcVnDf+iz'
    }

    target_url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='

    res = requests.post(target_url, headers=header, data=data)
    print(res.text)



    # with open('买条街.mp4', 'ab') as f:
    #     f.write(res.content)
    #     print('success')

def main():
    url = input('please input your url:')
    get_url(url)






if __name__=='__main__':
    main()

