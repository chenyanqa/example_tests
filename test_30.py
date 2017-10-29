#!/usr/bin/env python
# -*- coding:utf-8 -*-

#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

s = input('请输入一个5位数：')
if len(s) != 5:
	print('输入的数字位数不对')
else:
	print('您的输入为%s'% s)

	if s[0] == s[4] and s[1] ==s[3]:
		print('您输入的是回文数')
	else:
		print('您输入的不是回文数')