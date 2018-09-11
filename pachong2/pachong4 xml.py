#xml 就是传数据   w3school
#xpath  是一门查找信息的工具  w3cschool 开发工具chrome插件 百度安装
'''
1.常用路径表达式：选取此节点的所有子节点
/:从根节点开始
//:选取元素，而不考虑元素的具体为止
.  :当前节点
.. :父节点
@ ：选取属性

2. 谓语（predicates）
    谓语用来精确查找
    /bookstore/book[1] :选取第一个属于bookstore下的叫book的元素
    /bookstore/book[last()]: 选取最后一个
    /bookstore/book[last()-1]:选取最后第二个
    /bookstore/book[position()<3]  选取前两个
    /bookstore/book[@lang]: 选取含lang的属性
    /bookstore/book[@lang='cn']: 选取含lang=cn的属性的元素
    /bookstore/book[@price<90]: 选取含price中小于90的属性的元素
    /bookstore/book[@price<90]/title: 选取含price中title标签中小于90的属性的元素

3.通配符
- *  ：任何元素节点
- @* :匹配任何属性节点
- node（）：匹配任何类型的节点

4.选取多个路径
- //book/title   | //book/author :选取book元素中title和author元素
- //title  |  //price  :选取文档中所有的title和price元素




#lxml库
- python的html/xml 的解析器
官方文档： http://lxml.de/index.html
案例如下

'''
from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"> <a href="0.html">first item</a> </li>

</ul>
</div>
'''
html = etree.HTML(text)
s = etree.tostring(html)
print(s)

html0 = etree.parse("pa.html")
print(type(html0))
rst0 = html0.xpath("//book")
print(rst0)
rst1 = html0.xpath('//book[@category="learn"]')  #谓语用中括号
print(rst1)
rst1 = html0.xpath('//book[@category="learn"]/year')  #谓语用中括号
rst1 = rst1[0]
print(rst1.tag)    #打出标签year
print(rst1.text)    #打出标签内容2018

print(rst1)
rst = etree.tostring(html,pretty_print=True)
print(rst)


