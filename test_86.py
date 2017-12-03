#!/usr/bin/env python
# -*- coding:utf-8 -*-

#两个字符串连接程序。
if __name__ == '__main__':
	a = "acegikm"
	b = "bdfhjlnpq"

	# 连接字符串
	c = a + b
	print(c)

	d = ''.join([a,b]) #join()函数中只能有一个序列参数
	print (d)