from urllib import request,parse
from http import cookiejar
cookie = cookiejar.CookieJar()  #创建一个实例

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
    req = request.Request(url,data=data.encode())
    rsp = opener.open(req)



if __name__ == '__main__':
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
#handler是Handler的实例，常用的有上面3个handler，用来处理复杂请求，每个hangler负责一块内容
#创立handler后，使用opener打开，打开后相应的handler由相应的处理
#cookie作为一个变量打印出来
