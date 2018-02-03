#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、MIME类型：它全名叫多用途互联网邮件扩展（Multipurpose Internet Mail Extensions），最初是为了将纯文本格式的电子邮件扩展到可
以支持多种信息格式而定制的。后来被应用到多种协议里，包括我们常用的HTTP协议。MIME的常见形式是一个主类型加一个子类型，用斜线分隔。比如
text/html、application/javascript、image/png等。在访问网页时，MIME type帮助浏览器识别一个HTTP请求返回的是什么内容的数据，应该
如何打开、如何显示。

2、模拟如何通过QQ邮箱给其他邮箱发送邮件，QQ邮箱得实现开启 smtp的服务，QQ邮箱POP3的端口号995,SMTP的端口号是465或587
https://www.cnblogs.com/lovealways/p/6701662.html

3、普通的SMTP 会话或者连接 是不经过加密的 一般端口默认是25，但是保险和安全性不好，SMTP_SSL是经过 ssl协议加密的，默认端口一般为465

4、如果邮件包含附件的话，则需要创建一个MIMEMultiple类型的邮件对象，然后将邮件正文 定义为MIMEText（）类型，然后attach到主邮件类型上
，然后定义一个MIMEBase（）的实例 去代表一个附件，同样也绑定到主邮件对象上

5、邮件的msg 内容 可以包含邮件正文、主题、收、发件人、附件、消息头等信息 这些都是有email模块负责创建，然后结合smtplib模块 创建一个
SMTP（host、port）的发件服务连接，然后先登录，然后在调用sendemail（）操作，最后退出即可
'''
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import smtplib

# #输入email的地址和口令
# from_addr = '879167367@qq.com'  #发送方邮箱
# password = 'rmjjpmrcrisybbeb'    #发送方邮箱的授权码
# to_addr = 'chenyan2011abc@sina.com'  #收件人邮箱
# smtp_server = 'smtp.qq.com'    #发件邮箱服务器
#
#
# #__init__(self, _text, _subtype='plain', _charset=None, *, policy=None)
# # _subtype is the MIME sub content type, defaulting to "plain".
# subject ='python邮件测试'
#
# # #纯文本邮件
# # msg= MIMEText('hello,send by python...,111111','plain','utf-8')
#
# #html类型邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>','html','utf-8')
#
# #发送邮件的主题、收件人、发件人等需要添加到msg中 一起发送，且这三个字段是固定的
# msg['Subject'] = subject
# msg['From'] = from_addr
# msg['To'] = to_addr
#
# #__init__(self, host='', port=0, local_hostname=None, timeout=<object object at 0x10213d150>, source_address=None)
# server = smtplib.SMTP_SSL(smtp_server,465)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()




#邮件包含附件的情况

from email.mime.multipart import MIMEMultipart  #自动导入模块快捷键
from email.mime.base import MIMEBase


from_addr = '879167367@qq.com'  #发送方邮箱
password = 'rmjjpmrcrisybbeb'    #发送方邮箱的授权码
to_addr = 'chenyan2011abc@sina.com'  #收件人邮箱
smtp_server = 'smtp.qq.com'    #发件邮箱服务器
subject ='python邮件测试'

#邮件对象（带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身）
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

#邮件正文
msg.attach(MIMEText('send with file...','plain','utf-8')) #将MIMEText实例绑定到 msg实例上

#添加附件（就是加上一个MIMEBase类，从本地读取一个图片）
with open('/Users/user/Documents/python/example_tests/test1.jpg','rb') as f:
    #MIMEBase 表示附件的类
    mime = MIMEBase('image','jpg',filename='test1.jpg') #_init__(self, _maintype, _subtype, *, policy=None, **_params)
    mime.add_header('Content-Disposition', 'attachment', filename='test1.jpg')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server,465) #经过ssl协议加密的smtp服务连接 ，默认端口是465
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()







