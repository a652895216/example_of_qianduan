# # cookie 自动使用
# CookieJar :管理存储cookie,想传出的http请求添加cookie
# cookie存储在内存中，CookieJar实例回收后cookie将消失
#     FileCookieJar（filename，delayload=None，policy=None）
#          使用文件管理cookie
#          filename是保存cookie的文件

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
    req = request.Request(url, data=data.encode())
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/334985193/profile"
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp.html", "w",encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()







