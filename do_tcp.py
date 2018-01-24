#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、socket是网络编程的一个抽象概念，我们用socket 表示打开一个网络连接，而打开一个socket需要知道目标计算机的ip
地址和端口号，在定制协议类型即可
2、大多数连接都是靠的tcp连接，且必须知道被访问服务器的ip地址及端口号，且端口号1024之前的服务是可以被固定的，例如
80是web服务的标准端口，smtp服务的端口是25，ftp是21等
3、一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket
4、但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。
'''

#建立一个tcp连接的Socket
import socket

# #AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# #发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# # 关闭连接:
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)



#创建一个基于ipv4、tcp的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接,connect(address)，对于ip-socket address参数必须是一个tuple是一对，例如 ('127.0.0.1',5678)
s.connect(('127.0.0.1',5678)) #这里的端口 为 当前所请求的服务的监听端口
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8')) #接收来自socket套接字缓冲区的byte数据

# 发送数据:
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
