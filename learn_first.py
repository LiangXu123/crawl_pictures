# coding=utf-8
# 徐亮的学习python爬虫,基础部分实践
#参考网址:http://aljun.me/post/17
import urllib
import urllib2

#LABEL-1
#得到一版面的 HTML代码
response=urllib.urlopen("http://www.jj20.com/bz/dwxz/")
#print response.read().decode('gb2312').encode('utf-8')

#LABEL-2
#w更高级的网站还需要我们伪造请求头信息,看网页源码中的请求头信息即可得到
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Host":"www.jj20.com"
}
request=urllib2.Request("http://www.jj20.com/bz/dwxz/",headers=header)
response=urllib2.urlopen(request)
print response.read().decode('gb2312').encode('utf-8')
#现在和LABEL-1的效果一模一样
#更复杂的还需要构造cookie,这里不追究具体方法,

#LABEL-3
#暴力从一张图片的网址下载图片
response=urllib2.urlopen("http://zhaduixueshe.com/static/pic/discovery.png")
with open("first.png","wb") as f:
    f.write(response.read())
#这种方法有时图片较大，这样下载很容易出现错误，这个时候我们需要缓存的帮助
import urllib2
import StringIO
response=urllib.urlopen("http://zhaduixueshe.com/static/pic/discovery.png")
response=StringIO.StringIO(response.read())
with open("second.png","wb") as f:
    f.write(response.read())

#LABEL-4
#最好用的下载图片的办法,
import urllib
path="best.png"
url="http://zhaduixueshe.com/static/pic/discovery.png"
urllib.urlretrieve(url,path)

