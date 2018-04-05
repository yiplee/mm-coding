#coding=utf-8
'''获取整个页面数据'''
#先获取要下载图片的整个页面信息
import urllib
import re
import time
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
# html=getHtml('http://image.so.com/i?src=360pic_strong&z=1&i=0&cmg=50f380bd75c3951992b1d722990300e2&q=%E6%97%A0%E9%99%90%E6%8C%91%E6%88%98%E5%9B%BE%E7%89%87')
# print html

def Schedule(blocknum,blocksize,totalsize):
        percent=100.0*blocknum*blocksize/totalsize
        if percent>100:
            percent=100
        return "%.2f%%" % percent

#该函数用于在获取的整个页面中筛选需要的图片连接
def getImage(html):
    error_time=0
    reg=r'src="(.+)?\.jpg" pic_ext'
    #该方法把正则表达式编译成一个正则表达式对象
    imgre=re.compile(reg)   
    #读取html中包含imgre（正则表达式）的数据
    imglist=re.findall(imgre,html)   
    #把筛选的图片地址通过for循环遍历并保存到本地
    #return imglist

    x=0
    while True:
        time.sleep(1)
        try:
            for imgurl in imglist:
                urllib.urlretrieve(imgurl,'%s.jpg' % x,Schedule)
                x+=1
        except:
            error_time+=1
            if error_time==100:
                print 'your network is little bad'
                time.sleep(60)
            if error_time==101:
                print 'your network is broken'
                break
            continue
        break
    # return imglist

    
html=getHtml('http://tieba.baidu.com/p/2460150866')
print getImage(html)


