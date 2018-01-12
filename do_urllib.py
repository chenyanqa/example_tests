#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#1\urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
#2\urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>
#3、rllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的
# 请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。



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
#     print(f.info()) #一般是 获取头信息
#     print(f.geturl()) #获取真实的url 可能

    # print(f.__dict__) #可以查看当前响应资源f 中的相关属性
    # print(dir(f))  #包括属性和方法
    # print('Status:',f.status,f.reason)
    # print ('----------')
    # print(f.getcode())
    # print(f.info())  #主要是请求header信息
    # print(f.geturl())
    # print ('----------')
    #
    # '''
    # getheaders() method of http.client.HTTPResponse instance
    # Return list of (header, value) tuples.
    #
    # getheader(name, default=None) method of http.client.HTTPResponse instance
    # Returns the value of the header matching *name*.
    # '''
    # #print(f.getheaders())
    # for k,v in f.getheaders():  #打印HTTP请求的头信息
    #     print('%s:%s'%(k,v))
    # print('Data:',data.decode('utf-8')) #打印HTTP响应的返回数据，json格式,由于信息在互联网上一般以bytes的形式传递，因此需要解码为str


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
#




#post发送请求（模拟微博登录）
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

2、Referrer的重要性
HTTP请求中有一个referer的报文头，用来指明当前流量的来源参考页。例如在www.sina.com.cn/sports/上点击一个链接到达cctv.com首页，那么就
referrer就是www.sina.com.cn/sports/了。在Javascript中，我们可以通过document.referrer来获取同样的信息。通过这个信息，我们就可以知
道访客是从什么渠道来到当前页面的。这对于Web Analytics来说，是非常重要的，这可以告诉我们不同渠道带来的流量的分布情况，还有用户搜索的关键
词等，都是通过分析这个referrer信息来获取的。

3、parse.urlencode() 接收一些二元元组，并将这些元素转换为url可识别的字符串，例如

login_data = parse.urlencode([
    ('username',email),
    ('password',password),
    ('savestate','1'),
    ('r','http://m.weibo.cn/'),
    ('entry','mweibo'),
    ('client_id','')
])

print(login_data)  已经转换为字符串，如下：
username=chenyan2011abc%40sina.com&password=chen2987&savestate=1&r=http%3A%2F%2Fm.weibo.cn%2F&entry=mweibo&client_id=&

'''
# from urllib import request,parse
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context #全局取消ssl证书校验
# print ('Login to weibo.cn...')
# email = input('Email: ')  #获取用户输入的用户名和密码
# password = input('Password: ')
#
# #urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=<function quote_plus at 0x101f5a0d0>)
# #作用：Encode a dict or sequence of two-element tuples into a URL query string.
# login_data = parse.urlencode([  #将登陆所需参数元组转换为对应的字符串 （可先通过浏览器试一遍，然后看下必传的参数，然后仿造就行）
#     ('username',email),
#     ('password',password),
#     ('savestate','1'),
#     ('r','http://m.weibo.cn/'),
#     ('entry','mweibo'),
#     ('client_id',''),
#     ('ec',''),
#     ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# print(login_data)
# #username=chenyan2011abc%40sina.com&password=chen2987&savestate=1&r=http%3A%2F%2Fm.weibo.cn%2F&entry=mweibo&client_id=&
# # ec=&pagerefer=https%3A%2F%2Fpassport.weibo.cn%2Fsignin%2Fwelcome%3Fentry%3Dmweibo%26r%3Dhttp%253A%252F%252Fm.weibo.cn%252F
# print(type(login_data)) #<class 'str'>
#
# req = request.Request('https://passport.weibo.cn/sso/login') #可通过在浏览器上抓包得到 通用头部信息 显示Request URL:https://passport.weibo.cn/sso/login
# req.add_header('Host','passport.weibo.cn')#以下信息在请求头信息中都有展示 仿造类似的数据及格式即可
# req.add_header('Origin','https://passport.weibo.cn')  #请求头中的Origin属性仅仅用于Post请求，用来表示最初的请求是从哪来发起的
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# #请求头中的 Refer 参数表示我来自哪个页面来的，服务器可以借此获得一些额外的信息。
#
# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print ('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print ('%s:%s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))



#Handler
#如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
'''
1、openers 对象 用于获取一个url，一般常用的urlpen（）函数就是调用了系统默认的openers对象来处理的，其中
install_opener 用来创建默认的opener ，opener对象有个open（）方法
2、build_opener(*handlers)  用来创建一个特定的opener对象
备注： urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。


3、Basic Authentication 基本验证，为了展示创建和安装一个handler（处理器），我们将使用HTTPBasicAuthHandler，例如
Www-authenticate: Basic realm="cPanel Users"
客户端必须使用新的请求，并在请求头里包含正确的姓名和密码。
这是“基础验证”，为了简化这个过程，我们可以创建一个HTTPBasicAuthHandler的实例，并让opener使用这个handler就可以啦。

4、简易代理服务器之python实现
1)代理服务器
代理服务器是在client和server之间的一个服务器，一般起到缓存的作用，所以也叫缓存服务器。比如：
A ----(HTTP）----》 B ----（HTTP）----》 C
其中A是客户端，C是服务器端，那么B就是proxy server了，是代理服务器，也是缓存服务器：当A发起请求时要求获得C上的一个文件，需要先经过B，B
在自己的文件系统中寻找是否有A所请求的文件，如果有，就发给A，完成一次响应；如果没有，则在B上创建新的HTTP请求，发送到C，并将C的响应缓存到
文件中，同时回发给A。只要代理服务器B上存在A所需要的文件，就不必劳烦C重新发送响应，一定程度上减轻C的压力，同时减少响应时间。

2）http代理
常用代理工具：fiddler  charles等工具
原理：就是将原始请求发送到代理服务器上，其中可以将部分请求直接打到host已经配置好的路径下。例如：10.39.26.122 x.elong.com ，可实现对域名
x.elong.com的请求 都转发到机器10.39.26.122上（就可以实现线上环境、灰度环境等的隔离）

5、端口： -- 总体来说是用来表明某网络或者主机上不同服务的（门牌号）
1）每个网络都一个端口号的！端口包括物理端口和逻辑端口。物理端口是用于连接物理设备之间的接口，逻辑端口是逻辑上用于区分服务的端口。TCP/IP协议
中的端口就是逻辑端口，通过不同的逻辑端口来区分不同的服务。一个IP地址的端口通过16bit进行编号，最多可以有65536个端口。端口是通过端口号来标
记的，端口号只有整数，范围是从0 到65535。
2）一台拥有IP地址的主机可以提供许多服务，比如Web服务、FTP服务、SMTP服务等，这些服务完全可以通过1个IP地址来实现。那么，主机是怎样区分不同
的网络服务呢？显然不能只靠IP地址，因为IP 地址与网络服务的关系是一对多的关系。实际上是通过“IP地址+端口号”来区分不同
的服务的。    服务器一般都是通过知名端口号来识别的。例如，对于每个TCP/IP实现来说，FTP服务器的TCP端口号都是21，每个Telnet服务器的TCP端口
号都是23，每个TFTP(简单文件传送协议)服务器的UDP端口号都是69。任何TCP/IP实现所提供的服务都用知名的1～1023之间的端口号。这些知名端口号由
Internet号分配机构（InternetAssignedNumbersAuthority,IANA）来管理
3）就像你家的大门口，有的人知道门在哪才能进来，不知道的进不来。改了默认值，就进不去了。比如路由器默认端口80，有人改成8080，你就进不去了，
必须标明端口。，例如：http://www.example.com:8080/等

4）逻辑端口又分为：
公认端口（http服务-80，https服务-443，ftp-21等）
注册端口（也就是很多服务绑定在这些端口上，这些端口也用于很多其他目的）
动态端口（动态端口的范围是从1024到65535。之所以称为动态端口，是因为它 一般不固定分配某种服务，而是动态分配。动态分配是指当一个系统进程
或应用 程序进程需要网络通信时，它向主机申请一个端口，主机从可用的端口号中分配 一个供它使用。当这个进程关闭时，同时也就释放了所占用的端口号）



'''
#支持代理方式验证请求
# from urllib import request
# #ProxyHandler(proxies)参数proxies是一个字典，将协议名称（http，ftp）等映射到相应代理服务器的URL
# proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'}) #创建一个代理处理器
# proxy_auth_handler = request.ProxyBasicAuthHandler() #创建一个包含基本http验证的处理器
# #realm是与验证相关联的名称或描述信息，取决于远程服务器。uri是基URL。user和passwd分别指定用户名和密码。
# # add_password(self, realm, uri, user, passwd)
# proxy_auth_handler.add_password('realm','host','username','password')  #给这个基本验证处理器添加密码等信息
# opener = request.build_opener(proxy_handler, proxy_auth_handler) #使用这些定义好的处理器来生成一个opener实例
#
# with opener.open('http://www.example.com/login.html') as f:  #调用该实例的open（）方法 打开一个url并获取一个 http.client.HTTPResponse对象
#     print('OK')



# #基本的http验证，登录请求
# import urllib.request
# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib.request.HTTPBasicAuthHandler()  #创建一个实现http基本验证的处理器
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
# #如果自定义的opener 通过install_opener()方法安装后，则会将默认的opener都改为这个，此时若调用urlopen（）其实也是这个更新后的opener在
# #起作用，若不想全局改变所有的opener，则可以继续使用该opener.open()方法即可单独生效
#
# urllib.request.urlopen('http://www.example.com/login.html')



#练习题：利用urllib读取JSON，然后将JSON解析为Python对象：
from urllib import request
import ssl
import json

def fetch_data(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    req = request.Request(url)
    with request.urlopen(req) as f:
        # f_json = f.read().decode('utf-8') #f.read()刚读取出来的是bytes 类型，需要解码为str类型
        # return f_json  #返回的是 json串

        f_python = json.loads(f.read().decode('utf-8'))  #dumps（）将python对象转换为json串，loads（）从json串转换为python对象
        return f_python  #返回一个python对象，一般是一个字典（可以尝试转换为json是提示错误）


url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'

data = fetch_data(url)
print(data)
#这种data['']['']的读取方式时 python字典的方式，因此json串必需先转换为python对象才能正常读取数据
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')