#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、通过反复执行程序发现，每次执行，主进程（即父进程）都不同，即程序每执行一次，操作系统会重新分配一个进程来运行程序指令，该进程还可以调用
os.fork()函数来要求操作信息重新创建一个子进程。
2、os.fork()函数是python 里面唯一一个调用一次  返回2次数据的函数，非常特殊。
3、os.fork()函数的操作原理是，当进程调用fork函数时，操作系统会自动创建一个子进程，该进程就是对父进程的一个完全拷贝，包括全局&环境变量，
本质上与父进程完全一致，唯一的区别是fork（）的返回值不同，如果返回值大于0 ，则表示在父进程中，且该返回值为当前子进程的pid，如果fork（）
返回值=0，则表示当前在子进程中。
4、通过反复执行程序 发现，os.getpid() 表示获取当前进程id，而且if 和else 执行顺序不是固定的，因为子、父进程是并发执行的 相互独立的，其执行
顺序由操作系统的调度算法来决定
5、子进程是从fork（）调用后的指令开始执行。
6、有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时
，就fork出子进程来处理新的http请求。
7、windows 上不支持fork()调用
8、因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
'''
import os
print('Process (%s) strat....' % os.getpid())  #这个进程为 每次操作系统 为每个程序文件执行分配的，其父进程在同一个程序里面一般是不变的
print('Process (%s) parent is (%s)....' %(os.getpid(),os.getppid()))

pid  = os.fork() #fork()函数 调用一次， 返回2次

if pid == 0:
    print('I am child process (%s) and my parent is %s' %(os.getpid(),os.getppid())) #如果在子进程中，os.getpid()表示获取子进程id

else:
    print('I (%s) just created a child process(%s)' % (os.getpid(),pid)) ##如果在父进程中，os.getpid()表示获取父进程id

