#!/usr/bin/env python
# -*- coding:utf-8 -*-

#计算字符串长度。
'''
str为字符串
str.isalnum() 所有字符都是数字或者字母
str.isalpha() 所有字符都是字母
str.isdigit() 所有字符都是数字
str.islower() 所有字符都是小写
str.isupper() 所有字符都是大写
str.istitle() 所有单词都是首字母大写，像标题
str.isspace() 所有字符都是空白字符、\t、\n、\r
'''

while True:
	str = input('请输入字符及数字：')
	if str.isalnum():
		print(len(str))
		break
	else:
		print('输入有误,请重新输入')
		continue
