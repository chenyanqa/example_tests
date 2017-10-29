#!/usr/bin/env python
# -*- coding:utf-8 -*-
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
n = int(input('请输入月份：'))

# list = []
# list.append(1)
# list.append(1)
#
# for i in range(1,n-1):
# 	c = list[i-1]+list[i]
# 	list.append(c)
#
# print('当前月份兔子总数为：%d'%(list[n-1]))

def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

print(fib(n))