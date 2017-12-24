#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1、多任务可以由多进程完成，也可以由多线程完成，而且进程是由若干线程完成的，一个进程至少有一个线程
2、启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
3、Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，比较有局限性，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
4、由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个
current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命
名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
5、多进程与多线程的最大区别：多进程各自会有一份拷贝存在于每个进程中，因此各进程是互不影响，相互独立的，而多线程，则所有变量资源都是
共享的，因为任何一个变量都可以被任意一个线程修改，因此多线程同时该一个变量是，内容发生错乱
'''
import time,threading
import multiprocessing,os

def loop():  #创建的新线程需要执行的任务
	print ('thread %s is running...'%threading.current_thread().name) #current_thread()在主线程返回主线程信息，在子线程中则返回子线程信息
	print ('thread %s(%s)is running...' % (multiprocessing.current_process().name,os.getpid()))
	n = 0
	while n <5:
		n = n+1
		print ('thread %s >>> %s' %(threading.current_thread().name,n))
		time.sleep(1)
	print ('thread %s ended.'%threading.current_thread().name)

print ('thread %s is running...'%threading.current_thread()) #获取当前线程的整体信息（name、线程号等）
print ('thread %s is running...'%threading.current_thread().ident) #获取当前线程的id
print ('thread %s(%s)is running...' % (multiprocessing.current_process().name,os.getpid()))
t = threading.Thread(target=loop)
#由于新线程绑定的函数中 没有要求必须传入参数，因此可以不用传name，如果没有传的话，则name使用系统默认，例如Thread-1
#t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print ('thread %s ended.'%threading.current_thread().name)