#js加密， 当爬虫遇上反爬虫
#加密是在浏览器上js完成的，但是js可以直接读代码，看懂算法就可以破解。

#案例1：破解有道词典
from urllib import request,parse

def getsalt():
    import time,random
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt

def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))  #bytes的参数
    sign = md5.hexdigest()
    return sign

def getsign(key,salt):
    sign1='fanyideskweb'+ key + str(salt)+'???'
    sign2=getmd5(sign1)
    return sign2

def youdao(key):
    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getsalt()
    data={
         'i': 'girl',
         'from': 'AUTO',
         'to': 'AUTO',
         'smartresult': 'dict',
         'client': 'fanyideskweb',
         'salt': str(salt),
         'sign': getsign(key,salt),
         'doctype': 'json',
         'version': '2.1',
         'keyfrom': 'fanyi.web',
         'action': 'FY_BY_REALTIME',
         'typoResult': 'false'
    }
    data = parse.urlencode(data).encode()

    headers = {
    'Accept': 'application/json,text/javascript,*/*;q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': len(key),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'P_INFO=m13651972638@163.com|1524818435|0|other|00&99|shh&1524658040&other#shh&null#10#0#0|136638&1||13651972638@163.com; OUTFOX_SEARCH_USER_ID=-1315416440@10.169.0.83; JSESSIONID=aaalxRNhbbn8b7j2CRMvw; OUTFOX_SEARCH_USER_ID_NCOO=558189576.9835033; ___rl__test__cookies=1535026136512',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'

    }

    req = request.Request(url=url,data=data,headers=headers,)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
if __name__ == '__main__':
    youdao('girl')



#js在线转码 tool.oschina.net