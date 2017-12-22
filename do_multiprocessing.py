#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、multiprocessing 模块的主要功能之一是通过跨平台的多进程支持
2、Process（）进程类 创建实例的时候，需要绑定一个实例（子进程）需要执行的方法及参数，然后调用下start（）方法即可
例如：
def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

3、一般每个程序执行时，os 会重新给当前程序分配一个总的进程，这个进程的父进程一般就是os ，一般同一台电脑上固定是37128
4、如果该程序中 有创建子进程的操作，则该子进程一般是从父进程（即当前程序的总指挥进程）的下一个开始
5、p.start()方法 表示启动子进程
6、p.join()方法 表示等待子进程执行结束以后 在继续往下执行。
7、创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单

'''
from multiprocessing import Process  #从multiprocessing模块导入Process类
import os
import multiprocessing

# def run_proc(name):  #子进程需要执行的函数代码块- 需要在创建子进程的时候 绑定在子进程上
#     print('Run child process %s (%s)...' %(name,os.getpid()))  #获取当前子进程的信息
#
# if __name__ =='__main__':  #相当于主函数的作用
#     print('Parent process %s.' % os.getppid())  #相当于os级别的进程
#     print('Parent process %s.' % os.getpid())  #os 为整个程序执行分配的总进程
#     p = Process(target=run_proc,args=('test',))  #生成子进程
#     print('Child process will start.')
#     p.start()  #用start（）方法启动进程实例
#     p.join()  #join（）方法可以等待子进程结束后在继续往下运行，主要用于进程间的同步
#     print('Child process end')



# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getppid())  #应该是os 基本的进程，一般都不变，这个os进程为每个需要执行的程序分配一个进程来监控整个程序的执行
#     print('Parent process %s.' % os.getpid())
#     info('main line')  #执行这个程序前，还没有创建子进程，因此当前的进程还是os分配的全局进程
#     p = Process(target=f, args=('bob',))  #生成一个子进程
#     p.start()
#     p.join()

'''
main line
module name: __main__
parent process: 37128  #这个进程是系统为整个程序自动分配的进程，即当前整个程序的父进程
process id: 52947   # 相当于main函数代码块的执行进程
function f
module name: __main__
parent process: 52947  #由于是在主入口执行的，因此
process id: 52948
hello bob

'''


# print('Parent process %s.' % os.getpid())
# print('Parent process %s parent is (%s).' % (os.getpid(),os.getppid()))
#
# def f(name):
#     print('module name:', __name__)
#     print('parent process:', os.getppid())  #由于这个方法是绑定在创建子进程实例上的，因此其父进程就相当于是 整个os为整个程序分配的进程
#     print('process id:', os.getpid())  #这个就相当于是当前子进程实例的进程id
#
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

'''
Parent process 53839.
Parent process 53839 parent is (37128).
module name: __main__
parent process: 53839
process id: 53840
hello bob
'''

#利用Process（）类+循环的方式同时创建多个进程，但是这种方式针对数量较小时 还好，如果需要创建成千上万 就得用到Pool（）类
#Pool（）类的作用，相当于我创建一个
#Pool类讲解：http://blog.csdn.net/seetheworld518/article/details/49639651
def do(n):
    name = multiprocessing.current_process()
    print('%s Starting...' %name)
    print('worker %d'%n)
    return

if __name__ =='__main__':
    for i in range(5):
        p = Process(target=do,args=(i,))
        p.start()
        p.join()
    print('end...')