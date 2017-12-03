#!/usr/bin/env python
# -*- coding:utf-8 -*-

#时间函数举例3。
#Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用
if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print (i)
    end = time.clock()
    print('different is %6.3f' % (end - start))