import requests  #使用requests更加方便
from lxml import etree

url = "https://www.qiushibaike.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
rsp = requests.get(url, headers=headers)
# print(rsp.text)
html = rsp.text
html = etree.HTML(html)
rst = html.xpath('//div[contains(@id,"qiushi_tag_")]')
print(len(rst))
for r in rst:
    content = r.xpath('a[@class="contentHerf"]/div[@class="content"]/span')[0].xpath('string(.)').strip()
    #遇上<br>标签处理方式  .xpath('string(.)')
    # 注意子etree不能加// ， 不然是从头开始爬 ，错误示范：content = r.xpath('//a[@class="contentHerf"]/div[@class="content"]/span')[0].text.strip()
    print(content)

