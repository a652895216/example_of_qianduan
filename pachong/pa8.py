#UserAgent 伪装 用户代理，简称UA
from  urllib import request,error
if __name__ == '__main__':

    url ="http://www.4399.com"
    try:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    #伪装
        req = request.Request(url,headers=headers)

        # req = request.Request(url)
        # req.add_header("User-Agent","Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")

        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print('well-------------------------')

