#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1调试方法：print、assert，logging、pdb，IDE断点
2、写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
'''
#方法1：直接打印可能出错的变量取值，但是后面还得删除这个print语句，会产生垃圾信息
# def foo(s):
# 	n = int(s)
# 	print ('>>> n =%d'%n) #因为这里n是变量，而且很可能出错，所有将每次程序执行的时候将n的值打印出来，观察其取值是否正常
# 	return 10/n
# def main():
# 	foo('0')
#
# main()

#方法2：用assert断言
# def foo(s):
# 	n = int(s)
# 	assert n !=0 # 该表达式为真，则断言正常，否则断言失败
# 	return 10/n
# def main():
# 	foo('0')
#


# #方法3：logging模块,同时可以指定错误信息级别（debug，info，warning，error）
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' %n)
# print (10/n)

#方法4 ：启动pdb（python 调试器），让程序单步方式运行，可以随时查看程序,使用python -m pdb debug.py
#启动
s = '0'
n = int(s)
print(10 / n)

# #方法5 ：pdb.set_trace()
# import pdb #引入pdb模块
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)
#

#方法5 ：IDE的断点
