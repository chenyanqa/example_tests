#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 输出 9*9 乘法口诀表。

'''
python格式化输出时“
%s -- 表示字符串
%c -- 表示字符
%d -- 表示十进制整数
%f --表示浮点数 （% .2f 表示保留2位小数）

'''
for i in range(1,10):   #外层控制一共输出几行
	for j in range(1,i+1): #内层控制一行输出几个
		k = j*i
		print('%dX%d=%d'%(j,i,k),end=' ')  #使通过end 控制 print（）函数是否换行
	print()

