#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

s = input('请输入一个不超过5位数的数字：')
if len(s)>5:
	print('您输入的数字超过五位了')
else:
	n = int(s)
	print('您输入的数字为：%d，长度为：%d'% (n,len(s)))

	list = list(s)
	list.reverse()
	print('逆序数字为：%s'%list)

	s1=''.join(list)  #将列表转换为字符串的形势，"".join(list)，引号中是字符之间的分割符，如“,”，“;”，“\t”等等
	print('逆序数字为：%s' % s1)




