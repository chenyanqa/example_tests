#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''


# f0 = 0
# f1 = 1
# f2 = f0 + f1
# f3 = f1 +f2
#
# fn = f(n-1)+f(n-2)

# n = int(input('请输入斐波那契数列值：'))
# list = []
# f1 = 1
# list.append(f1)  #追加第一个元素 f1
# f2 = 1
# list.append(f2)  #追加第二个元素 f2
#
# for i in range(1,n-1):   #因为 f1、f2 已经在了 所以总循环数 需要去掉2个
# 	fi= list[i-1]+list[i]
# 	list.append(fi)
# print(list)

def fib(n):  #递归的思想，先用定义函数求fn 然后再定义函数过程中 使用调用当前函数去求f(n-1)
	if n ==1 or n ==2:
		return 1
	else:
		return fib(n-1) +fib(n-2)
print(fib(10))




