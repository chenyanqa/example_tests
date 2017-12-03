#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：八进制转换为十进制
#先来看八进制如何转换成十进制。其方法与二进制转换成十进制差不多：按权相加法，即将八进制每位上的数乘
# 以位权（如8,64,512….），然后将得出来的数再加在一起。
import  math
if __name__ == '__main__':

	list1 = []
	for i in range(3):
		list1.append(int(input('请依次输入八进制数：')))
	print(list1)
	n = len(list1)

	list2 = []
	for i in range(n):
		list2.append(list1[i] * pow(8, (n-1 - i)))
	print(list2)
	print(sum(list2))
