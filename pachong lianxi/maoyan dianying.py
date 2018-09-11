'''
用正则来爬猫眼电影
1.url：http://maoyan.com/board
'''

from urllib import request
url = "http://maoyan.com/board"
rsp = request.urlopen(url)
html = rsp.read().decode()
# print(html)

import re
s = r'<dd>(.*?)</dd>'   #非贪婪模式匹配
pattern = re.compile(s, re.S)
m = pattern.findall(html)
print(type(m))

for i in m:
    s = r'<a href="/films/.*" title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(i)[0]
    print(title)
    ss = r'<p class="star">([\S\s]*?)</p>'
    pattern = re.compile(ss)
    title = pattern.findall(i)[0]
    title = title.replace("\n", "")
    title = title.replace(" ", "")
    print(title)



