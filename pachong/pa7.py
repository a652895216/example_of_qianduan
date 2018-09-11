from urllib import  request,error
if __name__ == '__main__':
    url='http://www.baidu.com'
    try:  #用try万一出问题崩溃
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("Httperror:{0}".format(e.reason))
#httperror是对应的请求码错误 如www.baiiidu.com/
    except error.URLError as e:
        print("Error:{0}".format(e.reason))
        print("Eror.{0}".format(e))
        #Urlerror是网络出现问题
    except Exception as e:
        print(e)