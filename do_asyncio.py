#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、因为asyncio.sleep(1)是协程，协程在线程下可以切换执行，不会等待
2、yield from asyncio.sleep(5)  #这句话的意思是协程告诉调度器过5秒以后再来找我，然后就让出线程了。然后调度器接着干自己的活儿
，5秒以后 如果线程不忙的话 就用send（x）来唤起协程

3\@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），
然后接着执行下一行语句。把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，
因此可以实现并发执行。
'''

# import asyncio
#
# @asyncio.coroutine  #将一个generator 标记为协程 coroutine类型，然后把这个coroutine 扔到EventLoop中执行
# def hello():
#     print("Hello world!")
#     #把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
#     r = yield from asyncio.sleep(5)  #asyncio.sleep(1) 也是一个协程，
#     print("Hello again!")
#
# #asyncio是python中对异步IO的支持，编程模型就是一个消息循环，返回一个正在运行的Eventloop
# loop = asyncio.get_event_loop()
# #print(loop) #<_UnixSelectorEventLoop running=False closed=False debug=False>
# print('test')
# loop.run_until_complete(hello()) #把hello（）携程扔到Eventloop中执行
# loop.close()



# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1) #协程里面 遇到yield from 就先挂起当前协程，去执行消息循环-tasks里面的下一个协程
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# '''
# 1、由于tasks里面有2个协程，执行第一个时，先打印Hello world! 然后遇到语句yield from asyncio.sleep(2) 表示此处需要去调用另外一个协程，
# 但是此时主线程不会去等待这个协程的完成，因此立马中断，去找tasks 里面的另外一个协程去执行，如果asyncio.sleep(2) 执行完后，在切换来继续执行
# 当前协程
# '''
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

@asyncio.coroutine
def wget(host):
    print('wget %s ...'%host)
    connect = asyncio.open_connection(host,80)

    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield  from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



