import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def find_imgs(url, i):
    pass
        
    

def save_imgs(folder, img_addrs):   
    pass
    
    


def get_page(url, pages):
    
    num = []
    page_url = []
    
    html = url_open(url).decode('utf-8')
    print(html)

    
    return page_url

    

def download_mm(folder='ooxx', pages=5):

    if (os.path.exists('ooxx') == False):
        os.mkdir(folder)
    os.chdir(folder)
       
    img_addr = []
    i = 0
    
    url = 'http://www.ilovgou.com'

    pages_url = get_page(url, pages)
    
    '''
    img_addr = find_imgs(eacg_page_url, i)
    save_imgs(folder, img_addr)
    '''

if __name__=='__main__':
    download_mm()

