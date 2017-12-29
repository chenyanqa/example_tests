#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
2、multiprocessing.managers模块还支持把进程分布到多台机器上，一个服务进程可以作为调度者，将任务分配到其他多个进程中。
3、例如我们已经有一个通过Queue通信的多进程程序，现在由于执行任务的进程任务繁重，希望把发送任务进程和执行任务进程分布到两台机器上，通过managers
模块把原来的Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了
4、服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务
5、当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue
进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
6、Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。
7、
'''


#master 进程 将queue 注册到网上、生成并启动一个服务进程，然后设置任务
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue =queue.Queue()  #创建发送任务的队列
result_queue =queue.Queue()  #接收结果的队列

class QueueManager(BaseManager):  #从BaseManager继承的QueueManager，BaseManager(address，authkey)创建一个基础的server进程
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
#register(typeid[, callable[, proxytype[, exposed[, method_to_typeid[, create_method]]]]])
#typeid 是一个“类型标识符”，用于标识特定类型的共享对象。 这必须是一个字符串。 相当于是我提供网络上其他进程调用的进程名字（可共享的进程名）
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)


# 绑定端口5000, 设置验证码'abc'
manager = QueueManager(address=('',5000),authkey=b'abc') # 创建一个服务进程，绑定端口5000，且授权键为b'abc'

manager.start()

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,100)
    print('Put task %d...'%n)
    task.put(n)


print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result:%s'%r)

manager.shutdown()
print('master exit.')


# g = lambda :3  #相当于 无参数，只有表达式
# print(g())  # 输出为：3