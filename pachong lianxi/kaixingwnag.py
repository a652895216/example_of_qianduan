'''
登录开心网
用cookie
寻找登录入口：https://security.kaixin001.com/login/login_post.php
'''
from urllib import request,parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from http import cookiejar

cookie = cookiejar.MozillaCookieJar()  #创建一个实例 !!注意是mozilla

cookie_handler = request.HTTPCookieProcessor(cookie)  #生成cookie的管理器

http_handler = request.HTTPHandler()  #创建http请求管理器

https_handler = request.HTTPSHandler() #生成https管理器

opener = request.build_opener(http_handler,https_handler,cookie_handler)#创建请求管理器
#创立handler后，使用opener打开，打开后相应的业务由相应的handler处理


def login():
    url = "https://security.kaixin001.com/login/login_post.php"
    data = {"email":"13651972638",
            "password":"59627210"
            }
    data = parse.urlencode(data)
    headers = {
        "Content-length":len(data),
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = request.Request(url,data=data.encode(),headers=headers)
    rsp = opener.open(req)
    html = rsp.read()
    html = html.decode()


def gethomepage():
    base_url ="http://www.kaixin001.com/home/?_profileuid=181784014&t=47#"
    rsp = opener.open(base_url)
    html = rsp.read()
    html = html.decode()
    print(html)
if __name__ == '__main__':
    login()
    gethomepage()
