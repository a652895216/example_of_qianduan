from urllib import request,parse  #parse负责解析一些东西
if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'  #注意是/s?,这是参数设置
    word = input('input your keyword:')  #输入内容比如‘大熊猫’经过编码转化,一般中文进行转码其他不知

    dict1 = {
        'wd':word
    }                        #把输入的大熊猫编入字典
    qs = parse.urlencode(dict1)   #在把字典使用parse进行编码，转化成wd=%E5%A4%A7%E7%86%8A%E7%8C%AB的编码，这编码代表大熊猫在网页上的代号
    print(qs)
    fullurl = url + qs  #连接起来http与搜索内容
    print(fullurl)
    rsp =request.urlopen(fullurl)   #请求url
    print(rsp)
    html = rsp.read()
    html = html.decode('utf-8')  #是bytes
    # print(html)
    # 访问网络的两种方法 get post