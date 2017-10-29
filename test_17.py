#!/usr/bin/env python
# -*- coding:utf-8 -*-
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import re

'''
1、编码相关 decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，
表示将gb2312编码的字符串str1转换成unicode编码。 encode的作用是将unicode编码转换成其他编码的字符串，
如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。 

2、


'''
#方法1:通过遍历字符串的方式判断每个字符是啥，同时也可以统计中文
s = input('请输入一行字符：') #py3中input（）函数默认接收为字符串
a = 0
b = 0
c = 0
d = 0
for i in range(len(s)):   #由于本题的对象是字符串 因此可以直接用 for i in s：的方式来遍历
	if s[i].isalpha():  #python3 中字符串s 中若包含中文 也会被isalpha()识别上,在utf-8中 默认只占1位
		a = a+1
	elif s[i].isdigit():
		b = b+1
	elif s[i].isspace():
		c = c +1
	else:
		d = d+1
print('输入的字符串中包含%d个字母，%d个数字，%d个空格，其他字符%d个'%(a,b,c,d))



