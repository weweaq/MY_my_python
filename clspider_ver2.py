#####utf-8
import urllib.request
import urllib.parse
import os
import re
import sys,threading,time
import socket
class Bing:
    def openurl(self,url):
        tml=urllib.request.Request(url)
        tml.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        try:
            response = urllib.request.urlopen(tml)
            html = response.read()
            return html
        except:
            print(sys.exc_info())
            return None
        
    def analysis(self,html):
        jpg=[]
        if html!=True:
            ss=re.findall(r',imgurl:"(http://[^"]+?\.[jpeg]{3,4})&',html)

        return (ss,len(ss))
        
    def savejpg(self,jpglits):
        for x in jpglits:
            tie=x.split("/")
            if not os.path.exists(self.关键词+'//'+tie[-1]):  
                self.下载+=1
                threading.Thread(target=self.save,args=(x,tie[-1])).start()#创建线程 执行下载X连接内的图片任务
            else:
                self.跳过+=1
            
    def save(self,http,tie):
        try:
            socket.setdefaulttimeout(50)#########设置50秒连接超时
            urllib.request.urlretrieve(http,self.关键词+'\\'+tie)#下载网页图片
            self.完成+=1
        except:
            if  os.path.exists(self.关键词+'\\'+tie):
                os.remove(self.关键词+'\\'+tie)
            print (sys.exc_info()[0],sys.exc_info()[1],http)
            self.跳过+=1
        self.结束+=1

        if self.stop:
            print('还有%d个图片正在下载!!!!!!\r\n此次共下载 %d张图片!'%((int(self.下载)-int(self.结束),self.完成)))
            
    def getopen(self):
        self.关键词=input('请输入关键词')
        self.页面上限=input('请输入爬取的页数')
        self.页面=0
        self.结束=0
        self.跳过=0
        self.下载=0
        self.完成=0
        jpg=[0,0]
        self.stop=False

        if not os.path.exists(os.getcwd()+'\\'+self.关键词):
            os.makedirs(os.getcwd()+'\\'+self.关键词)
        for each in range(int(self.页面上限)):
            print('正在爬取第%d页上一页%d张图片'%(each+1,jpg[1]))
            url2 = 'http://cn.bing.com/images/search?&q=%s&FORM=R5IR3&first=%d'%(urllib.parse.quote(self.关键词.encode('utf-8')),self.页面+1)
            html = self.openurl(url2)
            
            html = html.decode('UTF-8')
           
            jpg=self.analysis(html)
            
            self.savejpg(jpg[0])

            if (int(self.页面上限)-1)!=each:
            
                self.页面=self.页面+jpg[1]
            else:
                self.stop=True
        
        print('总共爬取%d张图片 些许数量不准 可能是网络等原因导致下载不成功 爬取结束%d张,还有%d个线程正在运行,共错误跳过%d张'%(self.下载,self.结束,self.下载-self.结束,self.跳过))
        print('注意!此时可能有的图片单个线程还在下载,')

if __name__=='__main__':
    jpgg=Bing()
    jpgg.getopen()
