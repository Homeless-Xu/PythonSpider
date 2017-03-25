# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# 先登录知乎. 然后再抓取cookie. 这个cookie 很长一段时间是不会变的.

import urllib.request
import http.cookiejar
url = 'https://www.zhihu.com'
# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)
# 此处的open方法同urllib的urlopen方法，也可以传入request
reponse = opener.open(url)
for item in cookie:
    print('name: %s \nvalue: %s' % (item.name, item.value))