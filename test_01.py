#!/usr/bin/env python
# -*- coding:utf-8 -*-

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

m = 0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if(i != j) and (j !=k) and (k != i):  #三个数互不相等的表达式
				a = 100*i + 10*j +k
				print('无重复的三位数为：%s' %(a))
				m= m+1

print('总个数为：%s' %(m))