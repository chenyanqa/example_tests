#!/usr/bin/env python
# -*- coding:utf-8 -*-
#题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
#程序分析：999999 / 13 = 76923。

n = int(input('请输入一个奇数：'))
# list1 = ['9']*2  #['9','9']
# print(''.join(list1)) # 99   使用join（）方法时 list1中必须是字符 不能是int

list = ['9']
for i in range(1,20):
	list1 = list*i  #注意此处 i 不能取0
	a = ''.join(list1)  #变成字符串

	if int(a) % n == 0:
		print(a)
		break
	else:
		continue  #继续for循环的下一次迭代

