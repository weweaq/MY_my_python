import urllib.request
import re
import os
from bs4 import BeautifulSoup

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def find_img(soup, pages):
    num_a = []
    ads = []
    
    all_num = soup.find_all('ul',class_='oneline')
    
    for each in all_num:
        num_a.append(each.find_all('a'))

    for each in num_a:
        for each_num in each:
            for i in range(pages):
                if( i == 0 ):
                    ads.append('http://www.ilovgou.com'+each_num['href'])
                else:
                    ads.append('http://www.ilovgou.com'+each_num['href'].split('.')[0]+\
                               '_'+str(i+1)+'.'+\
                               each_num['href'].split('.')[1])
    return ads

def get_img_adrs(url):

    num_a = []
    ads = []

    for each in url:     
        html = url_open(each).decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')     
        num_a.append(soup.find_all('center'))

    for each in num_a :
        if (len(each[0].find_all('img')[0]['src']) == 56):
            full = 'http://www.ilovgou.com' + each[0].find_all('img')[0]['src']
        else:
            full = each[0].find_all('img')[0]['src']
        ads.append(full)

    return ads

##    for each in ads  :
##        print(each)  
##    return all_num[0].find_all('img')[0]['src']  // 



def save_imgs(folder, img_addrs):
    i = 0
    for each in img_addrs:
        i = i + 1
        filename = str(i)+'.jpg'
        print(each)
        with open (filename,'wb') as f:
            img = url_open(each)
            f.write(img)


            


def bs4_test1(folder='ooxx', pages=10):

##    if (os.path.exists('ooxx') == False):
##        os.mkdir(folder)
##    os.chdir(folder)

    img_addrs = []
    

    url = 'http://www.ilovgou.com/'
    html = url_open(url).decode('utf-8')

    soup = BeautifulSoup(html,'html.parser')

    ads = find_img(soup,pages)
    img_addrs = get_img_adrs(ads)
    for each in img_addrs:
        print(each)
##    save_imgs(folder, img_addrs)

    
#    img_addrs.append(get_img_adrs(ads, pages))
   

    






if __name__=='__main__':
    bs4_test1()


        

        
        

#print(all_num[0].find_all('a')[0]['href'])



#print(soup.find_all('ul',class_='oneline'))
#print(type(soup.find_all('ul',class_='oneline')))

    
'''
soup = BeautifulSoup(html,'html.parser')
 for title in soup.select('title'):
print (title.get_text())
'''
   






























#for tag in soup.find_all(re.compile("^b")):
#    print(tag.name)

#print(soup.select('p #link1'))    
#for string  in soup.stripped_strings:
#    print (repr(string))
#print(soup.title)
#print(soup.a)
#print(type(soup.a))
#print(soup.p.string)
#print(type(soup.p.string))
#print(soup.a.string)
#print(type(soup.a.string))
#print(soup.p.attrs)
#print(soup.prettify())
#print(html)
