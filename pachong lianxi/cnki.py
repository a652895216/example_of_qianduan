import requests

from urllib import parse
url = "https://study.163.com/courses-search?"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
dict1 = {
    'keyword': 'python'
}  # 把输入的大熊猫编入字典
qs = parse.urlencode(dict1)  # 在把字典使用parse进行编码，转化成wd=%E5%A4%A7%E7%86%8A%E7%8C%AB的编码，这编码代表大熊猫在网页上的代号
baseurl = url + qs
rsp = requests.get(baseurl, headers=headers)
print(rsp.text)




