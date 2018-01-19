#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

2、urllib 中有一个request的模块
3、dir(r)
['apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history',
'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status',
 'raw', 'reason', 'request', 'status_code', 'text', 'url']

4、get(url, params=None, **kwargs)
    Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

5、post(url, data=None, json=None, **kwargs)
    Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

6、在使用requests 模块请求url时，不能连着代理，否则会报错

7、requests 模块
1）一般使用requests.get(),requests.post()来请求指定url，同时可以通过params=或者json=字段来传递参数
也可以通过headers= 、cookies=等来指定请求头及cookies等数据，也可以通过timeout= 来指定请求超时时间
2）请求后 返回一个 对应的响应类 <class 'requests.models.Response'>  ，这个响应 有'json', 'links',  'ok', 'reason', 'request',
'status_code', 'text', 'url'等属性  可以直接读取响应的对应数据

'''

#1、通过GET访问一个页面
import requests

# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# #print(r.text)  #直接展示解码后的内容，可以进行编码,默认header
# print(r.content)  #r.content 里面的内容有byte 需要解码
#
#
# #2、GET方式+参数
# r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})  #get(url, params=None, **kwargs)
# print(r.url)  #https://www.douban.com/search?q=python&cat=1001
# print(type(r))  #<class 'requests.models.Response'>
#
#
# #响应为json 可以直接获取
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json()) #若当前响应为json格式 ，可通过.json()方法直接获取
#
#
# #定制headers
# r = requests.get('https://www.douban.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# #print(r.text)


#发送POST请求 (requests默认使用application/x-www-form-urlencoded对POST数据编码)
#post(url, data=None, json=None, **kwargs)
# r = requests.post('https://accounts.douban.com/login',data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.content)
# print(r.url)

#使用json参数发送post请求
r = requests.post('https://accounts.douban.com/login',json={'form_email': 'abc@example.com','form_password': '123456'})
print(r.content)
print(r.url)
print(r.headers['Content-Type'])

#定制cookie
# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies=cs)

#设置请求超时时间
#r = requests.get(url, timeout=2.5)

