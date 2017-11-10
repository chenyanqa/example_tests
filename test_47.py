#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#两个变量值互换。


# #方法1：代码块
#
# a = int(input('请输入第一个数：'))
# b = int(input('请输入第一个数：'))
#
# print('a,b的输入值为%d,%d' % (a,b))
#
# a,b = b,a
#
# print('a,b的互换后的值为%d,%d' % (a,b))


#方法2：程序调用

def transfer(a,b):
    a,b = b,a
    print('a,b的互换后的值为%d,%d' % (a, b))

n1 = int(input('请输入第一个数：'))
n2 = int(input('请输入第一个数：'))

transfer(n1,n2)