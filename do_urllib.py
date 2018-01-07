#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#1\urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
#2\urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>




# from urllib import request
# import ssl
#
# #python2.7以后打开使用urllib 打开https连接时 需要进行ssl证书验证，目前通用的方式时 全局取消证书验证
# ssl._create_default_https_context = ssl._create_unverified_context  #全局取消证书验证
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     # for line in f:
#     #     print(line.decode('utf-8'))
#     print(type(f))  #<class 'http.client.HTTPResponse'>
#     data = f.read()
#
#     print(f.__dict__) #可以查看当前响应资源f 中的相关属性
#     print(dir(f))  #包括属性和方法
#     print('Status:',f.status,f.reason)
#     print ('----------')
#     print(f.getcode())
#     print(f.info())  #主要是请求header信息
#     print(f.geturl())
#     print ('----------')
#
#     '''
#     getheaders() method of http.client.HTTPResponse instance
#     Return list of (header, value) tuples.
#
#     getheader(name, default=None) method of http.client.HTTPResponse instance
#     Returns the value of the header matching *name*.
#     '''
#     #print(f.getheaders())
#     for k,v in f.getheaders():  #打印HTTP请求的头信息
#         print('%s:%s'%(k,v))
#     print('Data:',data.decode('utf-8')) #打印HTTP响应的返回数据，json格式,由于信息在互联网上一般以bytes的形式传递，因此需要解码为str


# #模拟iphone6 去请求都豆掰首页
# from urllib import request
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')
# with request.urlopen(req) as f:
#     #type(req) ---- <class 'urllib.request.Request'>
#     #help(request.urlopen) ----Open the URL url, which can be either a string or a Request object.
#     print ('Status:',f.status,f.reason)
#     for k,v in f.getheaders():  #http请求中，头信息 包括通用头信息、请求头、响应头、实体头
#         print ('%s:%s' %(k,v))
#     print('Data:',f.read().decode('utf-8'))


#post发送请求（模拟微登录）
'''
Request Header:
Accept:*/*
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Content-Length:295
Content-Type:application/x-www-form-urlencoded
Cookie:login=8948961dff729de4991669d2adb9e7a4..._T_WM=b96a1fec43b2206ed39bcff193a2db42; M_WEIBOCN_PARAMS=uicode%3D20000174
Host:passport.weibo.cn
Origin:https://passport.weibo.cn
Referer:https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F
User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36

From Data:
username:chenyan2011abc@sina.com
password:chen2987
savestate:1
r:http://m.weibo.cn/
ec:0
pagerefer:https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F
entry:mweibo
wentry:
loginfrom:
client_id:
code:
qq:
mainpageflag:1
hff:
hfp:



1、origin主要是用来说明最初请求是从哪里发起的；
origin只用于Post请求，而Referer则用于所有类型的请求；
origin的方式比Referer更安全点吧。

2、
'''
from urllib import request,parse

print ('Login to weibo.cn...')
email = input('Email: ')  #获取用户输入的用户名和密码
password = input('Password: ')

login_data = parse.urlencode([  #准备登录需要的参数并编码为bytes类型 （可先通过浏览器试一遍，然后看下必传的参数，然后仿造就行）
    ('username',email),
    ('password',password),
    ('savestate','1'),
    ('r','http://m.weibo.cn/'),
    ('entry','mweibo'),
    ('client_id',''),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login') #可通过在浏览器上抓包得到 通用头部信息 显示Request URL:https://passport.weibo.cn/sso/login
req.add_header('Host','passport.weibo.cn')#以下信息在请求头信息中都有展示 仿造类似的数据及格式即可
req.add_header('Origin','https://passport.weibo.cn')  #请求头中的Origin属性仅仅用于Post请求，用来表示最初的请求是从哪来发起的
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#请求头中的 Refer 参数表示我来自哪个页面来的，服务器可以借此获得一些额外的信息。

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print ('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

