#!/usr/bin/env python
# -*- coding:utf-8 -*-

#求1+2!+3!+...+20!的和。

def factorial(n):
	if n ==1 or n ==2:
		return 1*n
	else:
		return n*factorial(n-1)  #这里返回的是具体计算结果，例如factorial(3) 返回6


list=[]
n = int(input('请输入n的值：'))
for i in range(1,21):
	c = factorial(i)
	list.append(c)

print(list)
print('sum:%s'%sum(list))   #求和计算 使用列表特别方便
