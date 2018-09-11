from urllib import request
if __name__ == '__main__':
    url = 'https://www.qiushibaike.com'
    rsp =request.urlopen(url)
    print(rsp.geturl())  #返回请求对象的Url， 例如https://jobs.zhaopin.com/402972316250003.html
    print('****--------------***')
    print(rsp.info())    #请求反馈对象的meta信息 例如：各种信息日期，内容，长度，等等头信息
    print('***------------------****')
    print(rsp.getcode()) #例如404,502
    html = rsp.read()
    html = html.decode('utf-8')  #是bytes