#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import asyncio
#
# @asyncio.coroutine  #将一个generator 标记为协程 coroutine类型，然后把这个coroutine 扔到EventLoop中执行
# def hello():
#     print("Hello world!")
#     #把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
#     r = yield from asyncio.sleep(1)  #asyncio.sleep(1) 也是一个协程，
#     print("Hello again!")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()



# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''
1、yield from connect 相当于
for writer, reader in connect:
    yield writer, reader
connect 返回了两个参数，所以这里应该是参数解包

2、在我理解看来yield from就是挂起执行,这个reader和writer都是connect的返回值,也就是说,挂着去执行connet这个方法(即连接上面的网址),
这边等待中,然后去执行其他的逻辑了,等这里connet成功会返回reader和writer继续执行

3、返回值是一对IO，分别代表读写，当执行获取header时，3个程序协同工作，互不影响，也因此不分先后，无需等待



'''

import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s ...'%host)
#     connect = asyncio.open_connection(host,80)
#
#     reader,writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield  from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#         # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()



