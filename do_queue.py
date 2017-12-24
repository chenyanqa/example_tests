#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、可见如果在实例化Process时不指定target，就会执行默认的run方法。
2、join（）方法作用：阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。
3、队列类似于一条管道,元素先进先出,进put(arg),取get()
4、放数据,Queue.put（）默认有block=True和timeout两个参数。当block=True时，写入是阻塞式的，阻塞时间由timeout确定。当队列q被
（其他线程）写满后，这段代码就会阻塞，直至其他线程取走数据。Queue.put（）方法加上 block=False 的参数，即可解决这个隐蔽的问题。
但要注意，非阻塞方式写队列，当队列满时会抛出 exception Queue.Full 的异常
5、	取数据(默认阻塞),Queue.get([block[, timeout]])获取队列，timeout等待时间
6、
1）from Queue import Queue这个是普通的队列模式，类似于普通列表，先进先出模式，get方法会阻塞请求，直到有数据get出来为止
2）from multiprocessing.Queue import Queue这个是多进程并发的Queue队列，用于解决多进程间的通信问题。普通Queue实现不了。例如来
跑多进程对一批IP列表进行运算，运算后的结果都存到Queue队列里面，这个就必须使用multiprocessing提供的Queue来实现

'''

from multiprocessing import Process,Queue  #这里的Queue 主要用于实现多进程通信，普通队列实现不了
import os,time,random
#
# #写数据进程执行代码
# def write(q):
# 	print ('Process to write:%s' % os.getpid())
# 	for value in ['A','B','C','D']:
# 		print ('Put %s to queue...' % value)
# 		q.put(value)  #向队尾插入一个元素
# 		time.sleep(random.random())   #random.random() 生成0和1之间的随机浮点数float ,例如：0.06616623628431162
#
# #读数据进程执行的代码
# def read(q):
# 	print ('Process to read: %s' % os.getpid())
# 	while True:
# 		value = q.get()  #队对头删除一个元素并返回，而且get方法一般会阻塞请求，直到有数据被取到
# 		print ('Get %s from queue.' % value)
#
# if __name__ =='__main__':
# 	q = Queue() #在父进程中创建Queue，并传给各个子进程，这里没事这是长度，表示队列无限长
# 	pw = Process(target=write, args=(q,)) #创建写进程
# 	pr = Process(target=read, args=(q,)) #创建读进程
#
# 	pw.start() #启动进程
# 	pr.start()
#
# 	pw.join()  #在读写操作中，必须写操作执行完，才能读，所有需要调用join（）方法 阻塞主进程，等待写进程执行完毕
# 	pr.terminate() #由于读进程是个死循环，所以需要终止




# from multiprocessing import Process
# import os, time, random
#
# def r1(process_name):
#     for i in range(5):
#         print(process_name, os.getpid())    #打印出当前进程的id
#         time.sleep(random.random())
# def r2(process_name):
#     for i in range(5):
#         print(process_name, os.getpid()  )   #打印出当前进程的id
#         time.sleep(random.random()*5)
#
# if __name__ == "__main__":
#         print ("main process run...")
#         p1 = Process(target=r1, args=('process_name1', ))
#         p2 = Process(target=r2, args=('process_name2', ))
#
#         p1.start()
#         p2.start()
#         p1.join() #阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。
#         #p2.join() #如果把p2 进程的join（）方法注销掉，会发现主进程在等待p1 进程完全执行完毕后 不会管p2是否执行完成，直接执行主进程
# 		#所以使用多进程的常规方法是，先依次调用start启动进程，再依次调用join要求主进程等待子进程的结束。
#         print( "main process runned all lines...")

import queue  #普通队列
q=queue.Queue(6)    #如果不设置长度,默认为无限长
print(q.maxsize)    #注意没有括号
q.put(123)
q.put(456)
q.put(789)
q.put(100)
q.put(111)
q.put(233)
print(q.get())
print(q.get())