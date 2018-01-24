#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、udp协议 主要用在对延时要求严格，对数据准确性要求并不那么高的行业，例如直播、游戏、视频
2、udp的协议 客户端发送数据前 可以不用先建立连接，服务器端因此也不用监听。
3、客户端使用sendto（）、recv（）收发数据，recv(buffersize[, flags]) -> data
4、服务端使用sendto（）、recvfrom（）收发数据，recvfrom(buffersize[, flags]) -> (data, address info)

'''

#server 端
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024) #返回sender's 发送的数据及地址
    print('Received from %s:%s.' % addr)
    # 服务器处理数据
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr) #将处理后的数据  发送给客户端




#客户端：
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_DGRAM表示连接为udp类型

for data in [b'Michael', b'Tracy', b'Sarah']: #网络上传输的数据  都必需要求是字节流 byte类型的
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))  #udp 发送数据前 无需创建连接，使用sendto（）方法直接发送数据及目标服务器地址
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()