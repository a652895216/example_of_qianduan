'''
1.构件代理群，每次访问，随机选取代理并执行
'''
from urllib import request,error
import random
proxy_list = [
    {"http":"39.74.61.145:8118"},
    {"http":"118.190.95.35:9001"},
    {"http":"118.190.95.43:9001"},
    {"http":"182.88.88.24:8123"},
    {"http":"121.31.136.243:8123"}
]      #免费代理大多数会挂掉
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)  # 创建proxyHandler
    proxy_handler_list.append(proxy_handler)

opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)  # 创建opener
    opener_list.append(opener)

url = "http://www.baidu.com"
try:
    opener = random.choice(opener_list)   #从代理列表中随机挑一个
    request.install_opener(opener)       #安装

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
