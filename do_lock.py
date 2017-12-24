#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有
线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

2、可以通过锁的概念，解决数据错乱问题，例如给某个任务上一把锁，同一时刻只有获取到这个锁的线程才能修改数据，并进行后续操作，其他线程
则需要继续等待直到拿到该锁，所有当前拥有锁的线程用完一定要记得释放，创建所通过threading.Lock()创建。通过.acquire()方法获取

3、with最多的 就是打开文件，和实现__enter__和__exit__  其他地方最好还是使用try-ecept 比较方便

4、锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代
码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，
可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

5、Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响，因此python中
多线程的并发在Python中就是一个美丽的梦。
6、多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。（死锁：由于程序可以存在多个锁，不同的线程持有不同
的锁，并试图获取对方持有的锁时，容易造成死锁）

7、多个线程同时使用到一个变量时,注意加锁;因为GIL锁的存在,同一时间只能有一个线程实行,真正意义上的多线程并发在Python中是个梦.

'''

import time,threading
import multiprocessing

balance = 0 #假定balance是银行存款
lock = threading.Lock() #创建一个线程锁实例，同一时刻只有一个线程持有该锁，进行数据修改，保持了数据的准确性

def change_it(n): #先存后取，结果应该为0：
	global balance
	balance = balance +n
	balance = balance -n

def run_thread(n):
	for i in range(100000):
		lock.acquire() #先获取锁（这个过程中 可能造成阻塞，直到获取到锁）
		try:
			change_it(n)
		finally:
			lock.release() #改完一定要释放锁

		# with change_it(n) as a:  #with最多的 就是打开文件，和实现__enter__和__exit__,这里不太方便穿件上下文管理器
		# 	a(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print (balance)

print (multiprocessing.cpu_count()) #4
