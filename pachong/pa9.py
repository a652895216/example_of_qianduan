# 代理服务器www.xicidaili.com  www.goubanjia.com
# 代理量要大不然会被封掉
# 1 设置代理地址 然后创建proxyhandler 创建
from  urllib import request,error
if __name__ == '__main__':
    url = "http://www.baidu.com"
    proxy = {'http': '124.158.4.3:8080'} #设置代理地址
    proxy_handler = request.ProxyHandler(proxy) #创建proxyHandler
    opener = request.build_opener(proxy_handler) #创建opener
    request.install_opener(opener)  #安装opener

    #现在如果访问url,就是用代理

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)

# cookie与session
# # 由于http不会记忆信息，因此cookie是给用户的凭证，session保存在服务器云端上的另一半
# # cookie保存在用户上，单个cookie不超过4，一般最多不超过20个
# # session存于云端服务器
