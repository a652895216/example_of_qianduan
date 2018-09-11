'''#Request-献给人类，更简洁，继承了urllib所有特征，使用方法一样
开源地址：
中文文档：
'''
import requests
url='http://www.baidu.com/s?'

keyword={'wd':'刘强东'}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
rsp = requests.get(url,params=keyword,headers=headers)   #等同于rsp = requests.request('get',url)
print(rsp.text)
print('---')
print(rsp.content)
print(rsp.url)
print(rsp.status_code)  #请求返回码

# rsp1=requests.request('get',url)  #第二种方法

#返回的东西和之前的不太一样，




