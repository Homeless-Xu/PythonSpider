#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ❌ 遇到... 验证码会话无效 :( ❌

 ❤️模拟登录❤️
 利用终端也是能登录网站的!!!
    # 就是让机器 模拟人在浏览器上登录的行为.
    # 实际上就是: 人通过浏览器登录网站,浏览器为我们做了哪些事情

# 为什么要模拟登录呢!!!
    # cookie里面可能带有token，这一次能用，下一次就不能用了，所以很尴尬，
    # 人工去拿cookie也太low了，你不可能每次都去人工的，
    # 一般模拟登陆比较稳定，自动化程度比较好。

# 易模拟登录页面
    # 没有验证码，非ajax异步加载。
    # 不定局限于pc端网页，app端、移动端一般做的反爬策略比较少，可以从这里入手.


# 📌数据发送方式📌 Post & Get
    # 多数网站需要登录. 登录就是发送一些数据给对方.
    # 网页数据发送方式有两种. GET 和 Post
    # Get 会在浏览器地址栏显示你提交的内容.
    # Post 不会在浏览器地址栏显示你提交的内容
    # 比如淘宝登录密码. 你肯定不希望显示在地址栏中.那就用Post方式.

# 📌http/https 报文 (很多字段组成)📌
    # 发送方式 (get/post)  POST
    # 网址                 www.0214.live
    # 连接形式             keep-alive
    # 支持的压缩解压格式   gzip
    # 支持的语言           zh-CN
    # Cookie ..........    很长一串
"""











# ❤️模拟登录❤️
# 使用浏览器的话. 浏览器会帮你自动发送cookie给对方.你可以不用每次都登录.
# 但是用脚本 就得自己处理cookie了.
# 还好 我们可以用 cookielib 这个库来方便的处理cookie.
# 现在可以来说模拟登录了.
# 把cookie 添加到http请求中.
# 向网站发送一个请求 (包括 url post)






# 📌知乎模拟登录📌
    # 经典分析视频 https://v.qq.com/x/page/o0381sjo10b.html

# 知乎已经成为了爬虫的训练场，
    # 本文利用Python中的requests库，模拟登陆知乎，获取cookie，保存到本地，
    # 然后这个cookie作为登陆的凭证，登陆知乎的主页面，爬取知乎主页面上的问题和对应问题回答的摘要。
    # 关于知乎验证码登陆的问题，用到了Python上一个重要的图片处理库PIL,如果不行，就把图片存到本地，手动输入。

# 抓包分析发现.  登录知乎需要三个参数. 帐号+密码+xsrf
    # 这个xsrf隐藏在表单里面，每次登陆的时候，应该是服务器随机产生一个字符串。
    # 所以要模拟登陆的时候，必须要拿到xsrf。
    # 这个xsrf 只要你请求登录页面. 就会给你的 只要提取出来就行 很简单.
    # 这个xsrf 是动态变化的!!! 每次都不一样.
        # <input type="hidden" name="_xsrf" value="b5d21b316413f33867bdd1a786ccd9e4">










# 1. 谷歌浏览器 隐身模式.(⌘⇧N)
     # 隐身模式各种插件都会失效,各种网站都要重新登录.
# 2. 打开 https://www.zhihu.com/  
     # 切换到登录界面 而不是注册界面.
     # 打开开发者工具 F12
# 3. 尝试输入一个错误的 帐号密码 点击登录
# 4. 查看Network面板 
    # 多了个 phone_num/email 请求. 看你是用邮箱还是用手机号登录
    # 点击这个请求 就会出现这个请求的详细信息
    # 主要看详细信息里面的 headers 部分
# phone_num 请求headers 部分详解
    # General          → 可看发送方式 GET/POST
    # response headers → 服务器返回的消息.
    # request headers  → 📌本机发起的请求. 
    # form data        → 📌表格信息, 账号 & 密码& _xsrf 三个重要参数

# ❤️requests 库❤️
# 名字意思就是请求, 可以非常简单的帮你发送网络请求.
# 把我们的登录信息加入到请求头中.然后用这个来发送请求.
# 首先导入模块: >>> import requests

# 构造 Request headers
# 📌User-Agent 参数📌
# agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    # 对方服务器通过这个参数来判断你是用 哪个浏览器,什么系统登录的.
    # 你可以修改这个参数,来欺骗对方服务器.
    # 比如有些视频网站. 
    # 你用手机看就给你提供html 视频.
    # 你用电脑看就给你提供flash视频
    # Mac 看flash 非常卡, 你就可以在电脑上修改这个参数,让对方给你html格式的视频.
    # 现成的有很多谷歌浏览器插件可以帮你快速切换 user-agent

# 📌Request headers 请求📌
# headers = {
#     "Host": "www.zhihu.com",
#     "Referer": "https://www.zhihu.com/",
#     'User-Agent': agent
# }

# 这个请求就是重点了
# 你要登录什么网站.








# ❤️Cookie & Session❤️

# Session 
    # 可以创建一段持续性的会话. 这个会话下所有的请求都会使用相同的cookie.

# 什么是Cookie
    # 你登录网站后,服务器会给你一串特定的数据.这串数据就代表你这个用户, 这串数据就是cookie
    # Cookie 可以看成账户密码.
    # 别人获取了你的cookie就可以用这个cookie登录你的帐号.
    # 📌你发送的每个请求中都带有cookie.📌 所以你不用一直重复登录某个网站
    # 📌爬虫中使用cookie可以跳过登录问题📌
    # 一旦cookie 失效,或者被删除 就得重新登录....

# cookie: 两种形式
    # 一种是内存中的. 浏览器关闭就失效.
    # 一种存在文件里. 有一定的时效.

# Cookie 作用
    # 你总不想每次打开一个网页就登录一次吧!!! 
    # cookie 可以让你在很长一段时间内不用重复登录某网站,极大提升上网体验
    # 如果我们要把登录获得的cookies保存起来，让爬虫直接读取，我们就不需要登录了!!!

    # 有些网站必须注册后才能看某些页面,你要抓取那些页面.自然也要先注册了.
    # 但是爬虫不会自动注册啊.
    # 这就需要你先注册好.登录进去.然后对方服务器就会给你一个cookie.
    # 这个cookie 就是对应你这个账户密码.
    # 只要你发送的请求中带有这个cookie. 对方就认为你已经登录了.



# Cookie 构成
    # Cookie是http消息头中的一个字段(属性)，
        # Cookie名字（Name）
        # Cookie的值（Value），
        # Cookie的过期时间（Expires / Max-Age），
        # Cookie作用路径（Path），
        # Cookie所在域名（Domain），
        # 使用Cookie进行安全连接（Secure）。
        # 前两个参数是Cookie应用的必要条件.
        # 🎈登录后 cookie 是不一样的. 但是cookie里的 name 和 value 是一样的🎈


# 爬虫处理 Cookie 
    # 📌Cookie 主要操作: 保存cookie到变量 / 保存cookie到文件 / 从文件加载cookie📌
    # 处理Cookie 可以用 cookielib/CookieJar模块;  还可以用 requests 模块
    # 📌📌requests 大法好，简单强大，强烈推荐。📌📌

# 🎈Cookie模块: Cookielib / Cookiejar 🎈
    # cookielib (py2) 等于 http.cookiejar (py3)
    # coolielib 可以保存内存中的cookie 并在爬虫发起请求时带上cookie.
    # cookielib 保存cookie 到文件有三种方式 推荐后面两种.
        # 1. FileCookieJar(filename)
            # 创建FileCookieJar实例，检索cookie信息并将信息存储到文件中，filename是文件名。
        # 2. MozillaCookieJar(filename)
            # 创建与Mozilla cookies.txt文件兼容的FileCookieJar实例。
        # 3. LWPCookieJar(filename)
            # 创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。

# 🎈Cookie模块: Requests🎈
    # 可以直接把 cookie 写在header里. 然后带上访问.
    
    # cookies = {
    #     'uid': '1349',
    #     'user_email': 'admin%40linsir.org',
    # }
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    #            'X-Requested-With': 'XMLHttpRequest',
    #        }
    # requests.get(url, cookies=cookies, headers=headers,)


# 📌Session & cookie 📌
    # HTTP协议是无状态的, 
    # 比如淘宝, 你在淘宝上点击某个购买链接. 淘宝是不知道谁点击了这个链接的.
    # 如果淘宝的服务器需要知道 是谁点击了这个链接,就需要用某种机制来识别具体的用户. 
    # 这机制就是session.
    # 任何人都可以有 session. 不管你有没有登录
        # 典型场景就是购物车.
            # 你去淘宝. 先不登录淘宝. 随便逛逛.添加几个东西到购物车.
            # 当你登录时候.发现这几个东西还在购物车里.这就是session的作用.提升用户体验.

# 如何识别注册了的客户呢. 这就靠cookie了.
# 每次http请求. 客户端都会发送相应的cookie 到服务器.
# 用户验证这种场合一般会用 session 

    # session 维持一段对话; cookie 识别用户.
    # 如果想要所有请求 都使用相同的cookies .就需要session 来创建一段持续性的对话.
    # session 是存在服务器上的 cookie是存在客户端上的.
   
# session 是一个抽象概念，“是一个会话状态”，不管你没有登录完整. 我知道是你而不是别人在和服务器交流.
# cookie 是一个实际存在的东西，是用来识别具体某个人.
# session是存在服务器的，用于区分会话和不同用户的访问


'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
'''
import requests
    # pip install requests  这个默认安装在 python2 版本下的.
    # pip3 install requests 这个才是安装在 Python3 版本下的.
try:
    import cookielib
except:
    import http.cookiejar as cookielib
    # 这个就是加载 cookielib了. 如果用的python3 就加载http.cookiejar 两个一样的功能.    
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


# 构造 Request headers
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
    # 创建一个持续性的会话. 会话里使用同样的cookie
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
    # 这个就是加载cookie文件?
except:
    print("Cookie 未能加载")




# 获取 xsrf 值
def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'https://www.zhihu.com'
        # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
        # 先获取到 某个网页整个源码. 
    html = index_page.text
        # 取出网页源码里面的文本.
    pattern = r'name="_xsrf" value="(.*?)"'
        # <input type="hidden" name="_xsrf" value="b5d21b316413f33867bdd1a786ccd9e4">
        # 用正则式匹配出 _xsrf 的 value
        # 这里的_xsrf 返回的是一个list.
        # 取出list里面的第一个数值. 也就是_xsrf[0]
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]




# 获取验证码
# 你输入帐号密码后.会出现验证码.
# 你换一个验证码. 再看network 下的数据包.就能只能怎么获取验证码了.

def get_captcha():
    t = str(int(time.time() * 1000))
        # 这个是带毫秒的时间撮.. 
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


def login(secret, account):
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.json()
        print(login_page.status_code)
        print(login_code['msg'])
    except:
        # 需要输入验证码后才能登录成功
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.json()
        print(login_code['msg'])
    session.cookies.save()

try:
    input = raw_input
except:
    pass


if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)