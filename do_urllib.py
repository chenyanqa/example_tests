#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#1\urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
#2\urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>




from urllib import request
import ssl

#python2.7以后打开使用urllib 打开https连接时 需要进行ssl证书验证，目前通用的方式时 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context  #全局取消证书验证
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    # for line in f:
    #     print(line.decode('utf-8'))
    print(type(f))  #<class 'http.client.HTTPResponse'>
    data = f.read()

    print(f.__dict__) #可以查看当前响应资源f 中的相关属性
    print(dir(f))
    print('Status:',f.status,f.reason)

    '''
    getheaders() method of http.client.HTTPResponse instance
    Return list of (header, value) tuples.
    
    getheader(name, default=None) method of http.client.HTTPResponse instance
    Returns the value of the header matching *name*.
    '''
    #print(f.getheaders())
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',data.decode('utf-8'))
