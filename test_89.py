#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

list = []
for i in range(7):
	#list.append(int(input('请输入1-50的数值：')))
	a = int(input('请输入1-50的数值：'))
	if a >1 and a <50:
		list.append(a)
		print ('*' * list[i])

	else:
		print ('输入不合理')
		break


