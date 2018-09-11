#百度F12
# http://fanyi.baidu.com/sug
# 1.利用data结构内容，然后用urlopen打开
from urllib import request,parse
import json
url = 'http://fanyi.baidu.com/sug'
data = {
    'kw':'girl'
}
data = parse.urlencode(data)#使用parse模块进行编码
print(data)

data = data.encode('utf-8')         #数据类型进行转换 将str转成bytes类型的，因为str不能用
print(type(data))

headers={
    'Content-Length':len(data)  #要修改这个参数
}
print(headers)

rsp=request.urlopen(url,data=data)         #通过url发出请求
json_data =rsp.read().decode('utf-8')         #进行解码读取 ，是json格式，所以还要进行装载
#输入的是一对编码
json_data=json.loads(json_data)   #进行装载
print(json_data)

for item in json_data['data']:
    print(item['k'],'---',item['v'])

