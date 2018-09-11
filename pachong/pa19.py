'''ajax请求
 异步请求
 一定会有url请求方法，可能有数据。
爬豆瓣  '''
from urllib import request
import json
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=40'
rsp = request.urlopen(url)
data = rsp.read().decode()
data1 = json.loads(data)
print(data1)
for i in data1:
    print(i)