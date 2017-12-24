#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1、在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，
不会影响其他线程，而全局变量的修改必须加锁。
2、python __dir__() 和__dict__() 区别：相当于dict属性是dir的一个子集，而且不是所有对象都有dict属性，但是都可以调用dir（）函数
1）dir(threading.local())、help(threading.local().__dir__())

2）help(threading.local().__dict__())

3,上面示例中每个线程都可以通过 global_data.num 获得自己独有的数据，并且每个线程读取到的 global_data 都不同，真正做到线程之
间的隔离
global_data = threading.local()  #定义一个ThreadLocal实例，ThreadLocal本身是全局的。
def show():
    print threading.current_thread().getName(), global_data.num

'''

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local() #每个线程可以利用它来保存属于自己的私有数据，这些私有数据对其他线程也是不可见的


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student1
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student1= name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()