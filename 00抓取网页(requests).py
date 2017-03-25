# -*- coding: utf-8 -*-


# 网站会对 request header 做一些限制，
  # 不是浏览器 不回复你, 就是为了反爬虫...
  # 就需要设置一个 User-Agent 来骗对方的服务器



# http 请求状态有很多种，大多数情况下 200 是我们理想中的状态，
# 我们用 requests 的一个 status_code 方法来判断是否访问成功，
# 然后使用 print 一下，相当于打印日志了，
# 当我们做大规模抓取的时候，print 显然不是一个很好的选择，
# Python 的 logging 模块能够更好的胜任这项工作，
# 为了方便起见，我们暂时使用简单直接粗暴的 print 来做代替 logging 的工作

# 由于网络原因，可能会出现访问超时的问题，
# 为了让代码更健壮，我们可以设置 timeout, 
# 同时，如果确定网页不需要重定向， 可以设置 allow_redirects=False

# 至此，我们完成了一个网页的抓取，并且做了相关的异常处理。





import requests

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
    }
    try:
        html = requests.get(url, headers=headers, allow_redirects=Fasle, timeout=3)
        if html.status_code == 200:
            print(url, '@ok200', str(time.ctime()))
            with open('content.html', 'wb') as fw:
                fw.write(html.content)
                fw.close()
        else:
            print(url, 'wrong', str(time.ctime()))
    except Exception as e:
        print(url, e, str(time.ctime()))

if __name__ == '__main__':
    url = "Example Domain"
    get_data(url)


