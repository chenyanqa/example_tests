#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1、很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
2、call(...): Runs a command, waits for it to complete, then returns
        the return code.
3、subprocess.PIPE实际上为文本流提供一个缓存区。直到communicate()方法从PIPE中读取出PIPE中的文本.要注意的是，communicate()
是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。

4、
1）subprocess.call(*popenargs, **kwargs)
运行命令。该函数将一直等待到子进程运行结束，并返回进程的returncode。如果子进程不需要进行交互（即只需要运行程序，不需要将运行结果
赋值、输出等）,就可以使用该函数来创建。
2）subprocess.Popen
subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。它的构造函数如下：
subprocess.Popen(args, bufsize=0, executable=None, \
                             stdin=None, stdout=None, stderr=None, \
                             preexec_fn=None, close_fds=False, shell=False, \
                             cwd=None, env=None, universal_newlines=False,\
                             startupinfo=None, creationflags=0)

handle = open(r'd:\tmp.log','wt')
subprocess.Popen(['ipconfig','-all'], stdout=handle)

'''
import subprocess

#创建子进程，且无需交互
# print ('$ nslookup www.pyhton.org')
# r = subprocess.call(['nslookup','www.python.org']) # retcode = call(["ls", "-l"])
# print ('Exit code',r)

#创建进程并进程其他交互
print('$ nslookup')
#subprocess.Popen()
#stdin stdout和stderr，分别表示子程序的标准输入、标准输出和标准错误
#subprocess.PIPE一个可以被用于Popen的stdin 、stdout 和stderr 3个参数的特输值，表示需要创建一个新的管道。
#subprocess.STDOUT一个可以被用于Popen的stderr参数的输出值，表示子程序的标准错误汇合到标准输出。
#subprocess.PIPE实际上为文本流提供一个缓存区。直到communicate()方法从PIPE中读取出PIPE中的文本.要注意的是，communicate()
#是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

