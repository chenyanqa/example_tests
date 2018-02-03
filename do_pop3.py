#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、SMTP 是邮件发送协议（如果邮件客户端 给出一个发送邮件的请求，通过SMTP将邮件发给收件人对应的邮箱），
   POP3/IMAP 是邮件接收协议（可以将邮件下载到本地 然后将邮件内容解析为用户可读的模式）
2、邮件发送分为两步：编辑邮件（email）、发送邮件（smtplib）
3、邮件收取也分两步：1）用poplib把邮件的原始文本下载到本地   2）email解析原始文本，还原邮件对象

'''

import poplib
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header

email = '879167367@qq.com'
password = 'rmjjpmrcrisybbeb'
pop3_server = 'pop.qq.com'


def guess_charset(msg):
    charset = msg.get_charset() #Return the Charset instance associated with the message's payload.
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


server = poplib.POP3_SSL(pop3_server,995)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
# 身份认证:
server.user(email)  #Send user name, return response
server.pass_(password) #Send password, return response,(response includes message count, mailbox size)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat()) #Get mailbox status，Result is tuple of 2 ints (message count, mailbox size)
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print('mails %s'% mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails) # 观察可知 最新的邮件为索引最大的邮件
resp, lines, octets = server.retr(index)  #retr是Retrieve（取回）的缩写，Result is in form ['response', ['line', ...], octets].

# lines存储了邮件的原始文本的每一行,是一个list类型
# 可以获得整个邮件的原始文本:
#print('lines %s'% lines)
msg_content = b'\r\n'.join(lines).decode('utf-8') #'\r\n' 回车、换行
print(type(msg_content))  #<class 'str'>
#print('msg_content :%s'% msg_content) #将lines 里面元素 按照回车换行的形式链接起来，join(list)

# 把邮件内容(str)解析为Message对象
msg = Parser().parsestr(msg_content)  #Create a message structure from a string.
print(type(msg)) #<class 'email.message.Message'>
print_info(msg) # 自定义函数

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
