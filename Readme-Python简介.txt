'' Python 两个版本: 2.x  和3.x  不兼容的!!!!!
'' 	❗️版本升级:  Mac 默认2.x,升级3.x:  brew install python3❗️
'' 	Python的灵魂在于 各种优秀的库.各种框架.  爬虫框架: Scrapy
'' 
'' 进入python环境: 
'' 	命令行输入: python → 
'' 	>>> 显示出三个箭头就进去了.  退出用 exit()
'' 	>>> print('hello, world') → hello world
'' 
'' ‼️ shell 方向键乱码 ‼️
'' 	^[[A^[[B^[[D^[[C 这些就是方向键盘的 acsll 码.
'' 	安装下 readline  就好了!!!!!!!
'' 	easy_install readline








# 遇到这个报错: urllib.request 是python3的用法.
# 你得看看你默认的 python 使用什么版本的.
  # 📌Mac 系统自带的python环境 默认启动路径是 /usr/bin         📌
  # 📌Mac 用户安装的python环境 默认启动路径是 /usr/local/bin   📌
  # 📌终端里 用python xxx.py 默认使用/usr/local/bin 下的python 📌
    # type python → python is /usr/local/bin/python
    # 说明默认使用的是用户安装的环境. 但是用户安装也会有好几个版本的.
  # 最简单的办法: 
    # 📌📌要用python3 执行命令时候 python3 xxx.py 📌📌
    # 📌📌要用python2 执行命令时候 python2 xxx.py 📌📌




Python 下的模块要重新安装的好像.
pip3 install requests




