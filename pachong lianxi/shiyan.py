import re
language = '''<tr><th>床前明月光</th><td>忧思独伤心</td></tr><tr>'''
# 正则表达式获取<tr></tr>之间内容
res_tr = r"<tr>(.*?)</tr>"
m_tr = re.findall(res_tr,language,re.S|re.M)
print (unicode(m_tr,"utf-8"))

res_th = r"<th>(.*?)</th>"
m_th = re.findall(res_th,line,re.S|re.M)
for mm in m_th:
    print(unicode(mm,"utf-8"))
res_td = r"<td>(.*?)</td>"
m_td = re.findall(res_td,line,re.S|re.M)
for nn in m_td:
    print(unicode(nn,"utf-8"))