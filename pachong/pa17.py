#ssl证书就是指遵守ssl安全套阶层协议的服务器数字证书，由美国公司开发，传输信息时就可以加密了。
#页面显示安全，表示走安全协议了，其他人不会搞到信息，这是由第三方公司担保，
#CA（certifacacteAuthority）是数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构
#遇上流氓情况用代码消除掉
from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context   #利用非认证的环境替换认证的环境，相当于忽略了安全层

url="https://www.12306.cn/mormhweb/"
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)