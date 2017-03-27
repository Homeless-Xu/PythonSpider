#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
🔵 整体结构分析: 🔵
    只有92页, 每页最多 30 个主题, 每个主题若干张照片.

页面网址结构: 
    http://www.meizitu.com/a/list_1_1.html
    ...
    http://www.meizitu.com/a/list_1_92.html


🔵 页面主题结构: 🔵
<ul class="wp-list clearfix">
<li class="wp-item">
    <div class="con">
        <div class="pic">
              <a target="_blank" href="http://www.meizitu.com/a/5511.html">
    <img src="http://mm.howkuai.com/wp-content/uploads/2017a/03/11/limg.jpg">
              </a>
        </div>
        <h3 class="tit">
    <a href="http://www.meizitu.com/a/5511.html" target="_blank">一波性感的妹子来了</a>
        </h3>
    </div>
</li>
........
</ul>


🔵 各主题网址结构: 🔵
    http://www.meizitu.com/a/5511.html
    http://www.meizitu.com/a/5510.html
    http://www.meizitu.com/a/5506.html
    ...

🔵 某主题照片结构: 🔵
<div id="picture">
<p>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第1张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/01.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第2张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/02.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第3张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/03.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第4张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/04.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第5张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/05.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第6张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/06.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第7张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/07.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第8张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/08.jpg"><br>
    <img alt="漂亮女学生在考虑穿什么鞋呢？ ，第9张" src="http://mm.howkuai.com/wp-content/uploads/2017a/03/06/09.jpg"></p>
</div>



🔵 我们要做的: 🔵
    1. 获取所有的 主题链接.
    2. 找出某主题 的所有照片链接.
    3. 下载所有照片.

'''


# ❤️❤️ ↓↓↓ 0: 依赖模块 ↓↓↓ ❤️❤️


import urllib.request          # 获取网页内容
from bs4 import BeautifulSoup  # 解析网页内容
import re                      # 正则式模块.
import os                      # 系统路径模块: 创建文件夹用
import socket                  # 下载用到?
import time                    # 下载用到?
from lxml import html
from lxml import etree  # 导入xpath
import requests
from urllib.request import urlretrieve

# 这里我们用到新的库. 用xpath来分析网页更加简单.


'''
🔵 中文乱码问题 ✔︎ 🔵
page = requests.get('http://www.meizitu.com/a/list_1_1.html')
get 获取请求. 也就是获取对方源码.

print(page.url)
→ http://www.meizitu.com/a/list_1_1.html
输出网页的网址

print(page.text)
→ 输出整个网页的源代码. 这里就出现乱码了!!!

先查询对方网址用的编码. 
print(page.encoding)
ISO-8859-1

改变编码成GB2312, 再输出就解决了!!!!
page.encoding = 'GB2312'
print(page.text)
'''


'''
# 🔵 把所有90个页面加到 数组里面. ✔︎ 🔵
# 为下一步做准备: 把90*30 所有的主题链接 加到数组里面.
page1_urls = []            # 定义一个数组,来储存所有主题的URL
for page in range(1, 92):
    # 1-140. 整个妹子图只有140页,注意下面缩进内容都在循环内的!
    url = 'http://www.meizitu.com/a/list_1_' + str(page) + '.html'
    # request = urllib.request.Request(url)
    page1_urls.append(url)
print(page1_urls)
'''


'''
# 🔵 获取某个主题的 URL和名称 ✔︎ 🔵

page = requests.get('http://www.meizitu.com/a/list_1_1.html')
# 用requests 模块 获取到网页源码.
page.encoding = 'GB2312'
# 脚本运行默认编码是utf-8, 对方网站用的编码是 GB2312
# 你要告诉脚本. page 变量里面的数据编码是GB2312的. 
# 这样脚本才会自动转成utf-8给你.不然就是乱码.
tree = html.fromstring(page.text)
# 把整个HTML文件结构化成DOM树,保存到变量tree中.
# 之后就可以用 xpath/css 来取出里面的元素了.  我们用 xpath.

url = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[1]/div/div/a/@href')
# print(url)  → ['http://www.meizitu.com/a/5511.html']
name = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[1]/div/div/a/img/@alt')
# print(name) → ['一波性感的妹子来了']
'''


'''
# 🔵 获取某个主题下的 第一张图片地址 & 照片数量 ✔︎ 🔵
page = requests.get('http://www.meizitu.com/a/5511.html')
# 用requests 模块 获取到网页源码.
page.encoding = 'GB2312'
tree = html.fromstring(page.text)
url = tree.xpath('//*[@id="picture"]/p/img[1]/@src')
print(url)
# ['http://mm.howkuai.com/wp-content/uploads/2017a/03/11/01.jpg']

PicNum = tree.xpath('//*[@id="picture"]/p/img')
aa = len(PicNum)
print(aa)
# 一张照片一个img标签. 所有照片都在p标签下.  用len() 就能获取元素长度. 也就是照片数量!!!
'''


'''
# 🔵 获取某个主题下 所有图片地址 ✔︎ 🔵
themeURLS = []
url = 'http://www.meizitu.com/a/5511.html'
page = requests.get(url)
page.encoding = 'GB2312'
tree = html.fromstring(page.text)

PicNumes = len(tree.xpath('//*[@id="picture"]/p/img'))
# print(PicNumes)

for num in range(1, PicNumes + 1):
    # 这里range 是不包含.最大值的. 所以会少一张图片. 加1就正常了.
    url = tree.xpath('//*[@id="picture"]/p/img[' + str(num) + ']/@src')
    themeURLS.append(url)
print(themeURLS)
'''


'''
# 🔵 if else 用法 🔵
# 如果 url 没有值. 那么就...
# if (url):
#     themeURLS.append(url)
# else:
#     print("hah")
#     pass
# print(themeURLS)
'''



# 🔵 所有主题. 所有照片的下载地址 🔵
# theme1url = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[1]/div/div/a/@href')
# theme2url = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[2]/div/div/a/@href')
# url = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[1]/div/div/a/@href')
# # print(url)  → ['http://www.meizitu.com/a/5511.html']
# name = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[1]/div/div/a/img/@alt')
# # print(name) → ['一波性感的妹子来了']
# .....


AllThemesPic_urls = []            # 定义一个数组,来储存所有主题的所有URL
for webpage in range(1, 2):
    weburl = 'http://www.meizitu.com/a/list_1_' + str(webpage) + '.html'
    print("❤️第" + str(webpage) + "页网址: " + str(weburl))
    page = requests.get(weburl)
    page.encoding = 'GB2312'
    tree = html.fromstring(page.text)
    webThemeNumes = len(tree.xpath('//*[@id="maincontent"]/div[1]/ul/li'))
    print("❤️第" + str(webpage) + "页主题数量" + str(webThemeNumes))

    for theme in range(1, webThemeNumes + 1 ):
        themeurl = tree.xpath('//*[@id="maincontent"]/div[1]/ul/li[' + str(theme) + ']/div/div/a/@href')

        # print(themeurl) 
        print("第" + str(theme) + "个主题网址:" + str(themeurl) )
        # 第1个主题网址:['http://www.meizitu.com/a/5511.html']斤斤计较

        themepage = requests.get(themeurl[0])
        # ❌❌❌❌❌ themeurl 是一个数组!!!!!!!❌❌❌❌❌❌
        # ❌❌❌❌❌ 这里是不能传入数组的!!!!!!❌❌❌❌❌❌

        # page11.encoding = 'GB2312'
        themetree = html.fromstring(themepage.text)

        PicNumes = len(themetree.xpath('//*[@id="picture"]/p/img'))
        print("📌当前个主题照片数量:" + str(PicNumes))
        for num in range(1, PicNumes + 1):
            # 这里range 是不包含.最大值的. 所以会少一张图片. 加1就正常了.
            url = themetree.xpath('//*[@id="picture"]/p/img[' + str(num) + ']/@src')
            # print(url)    →  ['http://mm.howkuai.com/wp-content/uploads/2017a/03/11/01.jpg']
            # print(url[0]) →  http://mm.howkuai.com/wp-content/uploads/2017a/03/11/01.jpg
            

            # 下载文件. urllib  urllib2 request 三个模块可以选择.
            # ❤️ ❤️ request 用法 ❤️ ❤️
            r = requests.get('http://mm.howkuai.com/wp-content/uploads/2017a/03/11/01.jpg')
            print(r.url)               # 查看对应的 URL
            print(r.status_code)       # 查看对应的 返回状态码
            print(r.encoding)          # 查看返回内容字符集
            # print(r.content)         # 以字节的方式响应内容，如img类型的字节流
            # print(r.request.headers) # 查看请求头
            with open("code3.zip", "wb") as code:
                code.write(r.content)
            # AllThemesPic_urls.append(url)
    # print(AllThemesPic_urls)

# 这里返回的居然是 403 难怪下载不下来. 
# 这就是这个妹子图难爬的原因了..
# 对方能不让爬虫爬图片 
# 无非就是那些，　ｕｓｅｒａｇｅｎｔ，ｒｅｆｅｒｅｒ，ｔｏｋｅｎ，ｃｏｏｋｉｅ
# ... 暂时先不管了...  
# 本项目 只剩下下载这一步了. 





