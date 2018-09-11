from urllib import request,parse
from http import cookiejar
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)  #创建一个实例 !!注意是mozilla

cookie_handler = request.HTTPCookieProcessor(cookie)  #生成cookie的管理器

http_handler = request.HTTPHandler()  #创建http请求管理器

https_handler = request.HTTPSHandler() #生成https管理器

opener = request.build_opener(http_handler,https_handler,cookie_handler)#创建请求管理器
#创立handler后，使用opener打开，打开后相应的业务由相应的handler处理

def login():
    url="http://www.renren.com/PLogin.do"
    data = {
        "email":"652895216@qq.com",
        "password":"59627210"
    }

    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())
    rsp = opener.open(req)

    cookie.save(ignore_discard=True, ignore_expires=True)      #前者表示即使cookie即使被丢弃也会被保存，后面的即使过期也会被保存


if __name__ == '__main__':
    login()

#cookie的保存
