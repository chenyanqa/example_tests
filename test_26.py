#!/usr/bin/env python
# -*- coding:utf-8 -*-

#利用递归方法求5!。

def factorial(n):
	if n ==1 or n ==2:
		return 1*n
	else:
		return n*factorial(n-1)

print(factorial(5))