#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

fp = open('test.txt','w+')
s = input('请输入字符串：')
fp.write(s.upper())

fp.seek(0)
print (fp.read())

fp.close()



