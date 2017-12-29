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

4、Python提供了threading.local模块，方便我们实现线程局部变量的传递
5、threading.local（）可以创建一个全局变量字典，此时该字典在主线程和子线程中存取值会不一样，主线程取全局值，但是在子线程中的取值
是取当前子线程创建时传过来的属性值。 而且还可以给该全局变量 绑定不同的属性。
6、创建全局ThreadLocal对象。每个线程都有一个单独的空间存放自己的内容，这个空间对于当前线程来说也是全局的，当前线程的所有函数都能访
问这个空间的内容。

'''

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local() #每个线程可以利用它来保存属于自己的私有数据，这些私有数据对其他线程也是不可见的
print(local_school.__dict__) # {}
local_school.name = 'hahaha'
print(local_school.__dict__)  #绑定属性或者是赋值：{'name': 'hahaha'}

# print(dir(local_school))

def process_student():
    std = local_school.student1  # 给全部变量local_school 绑定属性，生成一个局部变量 并赋值给std
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student1:
    local_school.student1= name
    process_student()

#创建子线程t1，它要完成的任务时process_thread，接收到的参数时'Alice'，且当前子线程的名字叫做Thread-A，如果不取名的话，默认叫Thread-1
#name是供thread调度用的，local_school不保存它， dir(local_school)可以发现没有这个属性
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


'''
1、由于 local_data 是全局变量 所以具有全局访问权，即主线程，子线程都可以访问他。但是这个变量的取值却跟当前线程的路径有关系，
即可以实现 主线程中local_data 取全局值，但是子线程中local_data的取值各自不同。

2、实现上述功能的奥妙 在于local类中内置的_path()方法，在每次local_data 取值前 会先看下当前线程的路径，如果是主线程，则返回
该变量的全局属性，如果是子线程，则返回该子线程的值，如果是第一次访问则 local_data为空，可以后续给该变量绑定其他属性，作为该线程
的局部变量

3、threading.local类的作用 所以线程都可以保存一个全局值，但是各自线程互不干扰

4、local_data 为全局变量，local_data.name 可以当做属性，在子线程中 可以当做局部变量

'''

# from threading import local, enumerate, Thread, currentThread  #enumerate枚举
#
# local_data = local()   #生产一个ThreadLocal()的实例（相当于一个全局变量字典）
# local_data.name = 'local_data111' # 给全局变量local_data 绑定一个属性，赋值
#
#
# class TestThread(Thread):  #自定义进程，只需改下run（）方法即可，否则可以使用默认的threading.Thread(target=)
#     def run(self):
#         print(currentThread())  #打印当前子线程
#         print(local_data.__dict__) #获取子线程下的全局变量local_data的属性
#         local_data.name = self.getName() #给子线程下的全局变量local_data 绑定属性并赋值
#         local_data.add_by_sub_thread = self.getName()
#         print(local_data.__dict__) #再次访问子线程下的 全局变量local_data的属性
#
#
# if __name__ == '__main__':
#     print(currentThread())  #<_MainThread(MainThread, started 140735206580224)>
#     print(local_data.__dict__)  #{'name': 'local_data'}
#
#     t1 = TestThread()
#     t1.start()
#     # print(currentThread())   # 子线程1：<TestThread(Thread-1, started 123145307557888)>
#     # print(local_data.__dict__) #{} 数据返回为空
#     # local_data.name = self.getName()
#     # local_data.add_by_sub_thread = self.getName()
#     # print(local_data.__dict__)  # {'name': 'Thread-1', 'add_by_sub_thread': 'Thread-1'}
#
#     t1.join()
#
#     t2 = TestThread()
#     t2.start()
#     t2.join()
#
#     print(currentThread())  # currentThread()在主线程中所以表示当前主线程 <_MainThread(MainThread, started 140735206580224)>
#     print(local_data.__dict__) #主线程中访问的是全局变量，因此当前local_data属性为 {'name': 'local_data111'}

