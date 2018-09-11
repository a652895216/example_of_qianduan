from urllib import request,parse
import json
baseurl = 'http://fanyi.baidu.com/sug'
data1 = {
    'kw':'girl'
}
data = parse.urlencode(data1).encode()


headers={
    'Content-Length': len(data)
}
req = request.Request(url=baseurl,data=data,headers=headers) #身份伪装

rsp=request.urlopen(req)
json_data1 =rsp.read().decode()
print(json_data1)
json_data2=json.loads(json_data1)
print(json_data2)

for i in json_data2['data']:
    print(i["k"],'----',i["v"])