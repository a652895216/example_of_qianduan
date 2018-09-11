'''页面解析与数据提取
-结构数据：先有结构，在搞数据
    json文件
    转成python
    xml文件：先转化成python类型（xmltodict），xpath，css选择器，正则不太好写
-非结构化数据：现有数据，再搞结构
    -文本
    -数字
    -邮箱地址等

    -html文件:正则，xpath，css选择器
'''
import re
s =r'([a-z]+) ([a-z]+) ([a-z]+)'    #a~z之间的字母，中间有个空格
pattern = re.compile(s, re.I)
m = pattern.match("Hello world wide web")  #match一次匹配
print(m)
s = m.group(0)                #表示匹配成功的整个字符串
print(s)
a = m.span(0)  #返回匹配成功的 整个字符串的跨度
print(a)

b= m.group(1)  #表示返回的第一个分组匹配成功的字符串
print(b)
b= m.group(3)  #表示返回的第二个分组匹配成功的字符串
print(b)
c = m.span(1)  # 返回第一个匹配成功的字符串跨度
print(c)
c = m.span(2)  # 返回第二个匹配成功的字符串跨度
print(c)
d = m.groups() #所有打印字符串
print(d)

#2. search  从指定位置查找          findall：全部匹配，返回列表   finditer：全部匹配，返回迭代器
# split：分割字符串，返回列表  sub：替换

s= r'\d+'
pattern = re.compile(s)
m=pattern.search("qwer1234wsad5678zxcv9000", 10, 320)    #最后的数字可以不加，表示直接到底
print(m.group(0))

z = pattern.findall("qwer1234wsad5678zxcv9000")
y = pattern.findall("qwer1234wsad5678zxcv9000", 10, 60)
print(z,y)

x = pattern.finditer('qwer1234wsad5678zxcv9000')
print(type(x))  #迭代器打印要用for循环
for i in x:
    print(i.group())

#匹配中文问题，中文是unicode，gbk等编码   中文unicode范围大致在【u4e00-u9fa5】间

ss = u'天青色等烟雨,而我在等你'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
aa = pattern.findall(ss)
print(aa)    #汉字匹配

#贪婪与非贪婪   1.贪婪模式：匹配越多越好   2.非贪婪：尽可能少匹配     python数量词默认是贪婪模式

#例如：查找文qwerrrrrrrrrrqwerrrqwerr
          #re=qwer*   贪婪模式为qwerrrrrrr  非贪婪qwe（r都可以没有）



