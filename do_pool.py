#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、pool ：用进程池的方式批量创建子进程
2、Process ：主要用于创建单个子进程，与父进程不同
3、fork（） ：主要用于将当前进程复制一份作为子进程，但是接受到的fork（）返回值为0
4、multiprocessing 模块里面 很多需要传递参数的地方 都是用的tuple类型

5、在使用Python进行系统管理时，特别是同时操作多个文件目录或者远程控制多台主机，并行操作可以节约大量的时间。如果操作的对象数目不大时，
还可以直接使用Process类动态的生成多个进程，十几个还好，但是如果上百个甚至更多，那手动去限制进程数量就显得特别的繁琐，此时进程池就派上
用场了。 Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求。如果池满，
请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求。

6、当进程池中任务队列非空时，才会触发worker进程去工作，那么如何向进程池中的任务队列中添加任务呢，进程池类有两组关键方法来创建任务，分别
是apply/apply_async和map/map_async，实际上进程池类的apply和map方法与python内建的两个同名方法类似，apply_async和map_async分别为
它们的非阻塞版本
7、两组向进程池分配任务的接口：apply/apply_async和map/map_async。apply方法每次处理一个任务，不同任务的执行方法（回调函数）、参数
可以不同，而map方法每次可以处理一个任务序列，每个任务的执行方法相同。

8、apply（）-每次添加任务后，会等到该任务拿到结果以后，在继续，而apply_async() 向进程池添加任务后，不用等任务结果直接执行主进程代码


'''
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task  %s (%s)...' %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name,(end-start)))

if __name__ =='__main__':
    #print(os.getppid())
    print('Parent process %s.' % os.getpid())
    #Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None),Returns a process pool object
    #进程池会先定义同时可供用调用的进程数量，然后如果有新的请求，会判断当前进程池是否已满，如果未满，可以立即执行该请求，如果
    #进程池已满，则此时会告诉用户先等待，待进程池 有空缺的时候 在讲该请求添加进入。使用python3 中一般使用apple_async()桌和apple_async()添加

    p = Pool(processes=4)   #表示创建一个进程池大小为4的进程池实例

    for i in range(5):
        p.apply_async(long_time_task,args=(i,))#表示依次向进程池中添加4个任务，任何第5个 先放在队列里面缓存。
        #p.apply(long_time_task, args=(i,))
        #time.sleep(1)
        '''
        1、如果这里加上休眠1秒后，则每往进程池里面加一个任务时，会先休眠一秒，则是该任务函数有足够的时间来返回结果了。所以会先打印执行结果
        然后在执行主进程的 print('Waiting for all subprocesses done...')，否则 没有这一秒的休眠，由于是非阻塞式的，我添加先添加完4个
        任务，然后将最后一个放在缓存队列里面，就会立即执行主进程后面的代码，可能这个时候任务的执行结果还没有返回，所以主进程的打印比任务
        结果打印要早
        2、如果任务函数也没有任何休眠，则可能第一个函数能立马拿到结果，然后释放进程池空间，然后靠后的几个进程的先后顺序就得拼人品了
        '''

    print('Waiting for all subprocesses done...')
    p.close() #关闭进程池 使其不在接受新的任务
    p.join()  #主进程暂时阻塞，等待所有子进程都执行完毕后在继续执行
    print('All subprocesses done.')


#apply（）阻塞的方式执行结果：相当于是顺序的 串行的一条一条的执行，apply()主进程会被阻塞直到函数执行结束
'''
Parent process 60865.
Run task  0 (60867)...
Task 0 runs 1.88 seconds.
Run task  1 (60866)...
Task 1 runs 2.32 seconds.
Run task  2 (60868)...
Task 2 runs 0.09 seconds.
Run task  3 (60867)...
Task 3 runs 2.43 seconds.
Run task  4 (60866)...
Task 4 runs 1.77 seconds.
Waiting for all subprocesses done...
All subprocesses done.

'''

#apply_async()非阻塞 异步的方式执行，也就是启动进程函数之后会继续执行后续的代码不用等待进程函数返回
'''
Parent process 61131.
Waiting for all subprocesses done...  
Run task  0 (61132)...
Run task  1 (61133)...
Run task  2 (61134)...
Run task  3 (61135)...
Task 0 runs 2.02 seconds. 
Run task  4 (61132)...   #由于进程池限制，最后一个进程只能先在缓存队列等着，只有当其中某个任务执行完成后，才能开始执行他。
Task 1 runs 2.17 seconds.
Task 2 runs 2.21 seconds.
Task 3 runs 2.69 seconds.
Task 4 runs 2.99 seconds.
All subprocesses done.
'''


# from multiprocessing import Pool
# from time import sleep
#
# def f(x):
#     print(x)
#     sleep(1)
#
#
# def main():
#     pool = Pool(processes=3)    # set the processes max number 3
#     for i in range(50):
#         result = pool.apply_async(f, (i,))
#
#     pool.close()
#     pool.join()
#
#     if result.successful():
#         print('successful')
#
# if __name__ == "__main__":
#     main()