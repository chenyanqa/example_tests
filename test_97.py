#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

fp = open('test.txt','a+')   #a+ 表示可追加并读写

while True:
	s = input('请输入字符：')
	if s != '#':
		fp.write(s)

	else:
		break

fp.seek(0)
print(fp.read())

all_the_text = open('test.txt').read()
print (all_the_text)

fp.close()









