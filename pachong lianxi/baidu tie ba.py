from urllib import parse,request
if __name__ == '__main__':
    qs = {

        'kw':'怪物猎人',
        'ie':'utf-8',
        # 'pn':'0'

    }
    baseurl= 'https://tieba.baidu.com/f?'
    urls=[]
    urls.append(baseurl+parse.urlencode(qs))
    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode('utf-8')
        print(html)

