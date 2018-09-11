#读取cookie
from urllib import request,parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()  #创建一个实例
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True) # !!!!!读取命令

cookie_handler = request.HTTPCookieProcessor(cookie)  #生成cookie的管理器

http_handler = request.HTTPHandler()  #创建http请求管理器

https_handler = request.HTTPSHandler() #生成https管理器

opener = request.build_opener(http_handler,https_handler,cookie_handler)#创建请求管理器
#创立handler后，使用opener打开，打开后相应的业务由相应的handler处理

def getHomePage():
    url = "http://www.renren.com/334985193/profile"
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp.html", "w",encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()























