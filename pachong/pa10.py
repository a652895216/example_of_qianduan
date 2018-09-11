#cookie
from urllib import request
if __name__ == '__main__':
    url='http://www.renren.com/334985193/profile'
    headers={
        "Cookie":"anonymid=jl6em09ghbjb98; _r01_=1; _de=EBF64DB04E461BCB7D49636C5D3D4B7E696BF75400CE19CC; ln_uact=652895216@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20120816/2100/h_main_lcYu_303c000040011375.jpg; depovince=GW; JSESSIONID=abccK-XsU1NJU6gdhGJww; ick_login=0042cbfd-8ddd-4fb6-9c79-c4ae7e1eeb08; jebecookies=89c6ab96-2db1-43fe-a19d-6919a8c267a1|||||; p=d0fb51f07a63ec9a991c2331c07f55843; first_login_flag=1; t=eb11e55967e116cac5b5150894c6431f3; societyguester=eb11e55967e116cac5b5150894c6431f3; id=334985193; xnsid=5c7e0686; loginfrom=syshome; jebe_key=2be76956-568c-4813-bfc6-4ec3b1ad0cf2%7C149f2b176e11e25f542e6e74523fd118%7C1536046530617%7C1%7C1536046530770; wp_fold=0"
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
    with open("rsp.html","w",encoding='utf-8') as f:  #windows下存在编码问题，所以要加encoding=‘utf-8’，
        f.write(html)
