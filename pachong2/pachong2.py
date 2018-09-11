#post案例，比url简单多了

import requests
from urllib import parse
import json
url = 'http://fanyi.baidu.com/sug'
data= {
    'kw':'girl'
}
print(type(data))
#因为url要求是bytes格式，所以要转成bytes格式，但是

headers={
    'Content-Length':str(len(data))      #要修改这个参数,int类型的不行，改成str类型
}
print(type(headers))
rsp = requests.post(url,data=data,headers=headers)   #这里data直接用字典格式
print(rsp.text)

# for item in json_data['data']:
#     print(item['k'],'----',item['v'])
