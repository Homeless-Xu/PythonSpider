# -*- coding: utf-8 -*-

# 浏览器输入网址就下载网页并显示给你.
# 终端怎么下载网页呢.  用 urllib2 是最方便的.

# 输入下面三行代码. 运行这个脚本 
# 就可以在终端显示出 某个网站的源代码了
# 这样一个网页就算被你爬下来了!! 很简单吧.
# 你要爬另一个网站. 只要改掉urlopen 双引号里面的网址就可以了.

import urllib2
response = urllib2.urlopen("https://www.0214.live")
    # 调用 urllib库 里面的 urlopen 这个方法,这个方法需要传入一个数据.一般都是网址.
    # 把 整个网页数据保存到 response 这个变量中.
    # 这行其实可以分成两行.
        # request = urllib2.Request("https://www.0214.live")
        # response = urllib2.urlopen(request)
        # 推荐大家这么写. 最终会有很多代码. 这样写逻辑上更清晰.
        # 先传入一个请求,  然后再打开网站
print response.read()
    # 读取变量的内容. 也就是整个网页的内容.













