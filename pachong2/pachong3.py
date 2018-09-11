#proxy 代理
import requests
proxies ={
    "http":"address of proxy"
    "https":"address of proxy"
}
rsp = requests.request('get',"http://www.baidu.com",proxies=proxies)


#代理服务器  格式用户名：密码@代理地址：端口

proxy = {"http":"a652895216：59627210@192.168.0.1:4444"}
rsp = requests.get("http://www.baidu.com",proxies=proxy)


#cookie requests可以自动处理cookie信息
rsp=requests.get("http://www.baidu.com")
cookiejar = rsp.cookies

cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
