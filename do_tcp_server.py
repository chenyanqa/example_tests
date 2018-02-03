#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、针对web服务，服务端会打开固定的80端口来监听客户端的连接，如果有客户端的请求（connect）过来，则服务端就与该客户端建立Socket连接，
后续的通信就靠这个socket 了，这个socket通过服务器地址、服务器端口、客户端地址和端口来唯一确定，同时为了同一时间响应多个客户端的请求，所以
每个连接都需要创建一个新的进程或者线程来处理

2、class socket(_socket.socket)
__init__(self, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, proto=0, fileno=None)
     |      Initialize self.  See help(type(self)) for accurate signature.


'''

import socket
import threading
import time

#基于ipv4 和tcp协议的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定监听地址和端口， 127.0.0.1 表示本机，端口大于1024即可，随机绑定
s.bind(('127.0.0.1',5678))  #bind(address)，the address is a tuple
#socket开始调用listen（）方法监听端口，5表示等待连接的最大数量,超过这个数量的连接可能会被拒绝
s.listen(5)
print('Waiting for connection...')

#定义服务端处理的内容和方式函数
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr) #这里的addr 形参到时候会接收当前实际监听到的客户端连接
    sock.send(b'Welcome!')

    while True: #持续不断 通过socket 接收客户端发过来的数据
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        #sock.send('Hello, %s!' % data) #TypeError: a bytes-like object is required, not 'str'
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True: #表示一直循环接收来自客户端的连接，accept（）会等待并返回一个客户端的连接
    #接收一个新的连接
    sock,addr = s.accept() #s.accept() 将返回一个新的套接字和客户端的地址，the address info is a pair (hostaddr, port)
    #创建新线程来处理tcp连接
    t = threading.Thread(target=tcplink,args=(sock,addr)) #这里的args=里面的参数 是提供给target后跟的方法使用的
    t.start()






