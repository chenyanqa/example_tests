#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# Monday  Tuesday  Wednesday  Thursday  Friday  Saturday Sunday

#方法1：方法一 没有实现主次输入
# s = input('请输入星期简称，首字母大写：')
#
# list1 = ['M','T','W','F','S']
# list2 = ['u','h','a']
#
# list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
#
# if s not in list:
# 	print('您输入的星期有误，请重新输入：')
#
# else:
# 	print('您当前的输入为：%s'%s)
# 	if s[0] ==list1[0]:
# 		print('星期一')
# 	if s[0] ==list1[2]:
# 		print('星期三')
# 	if s[0] ==list1[3]:
# 		print('星期五')
#
# 	if s[0] ==list1[1] and s[1] ==list2[0]:
# 		print('星期二')
# 	if s[0] ==list1[1] and s[1] ==list2[1]:
# 		print('星期四')
# 	if s[0] ==list1[4] and s[1] ==list2[2]:
# 		print('星期六')
# 	if s[0] ==list1[4] and s[1] ==list2[0]:
# 		print('星期日')


#方法2：字典的思路：:
# weeklist = {'M': 'Monday','T': {'u': 'Tuesday','h':'Thursday'}, 'W': 'Wednesday', 'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
#
# letter1 = input('请输入首字母：')
# letter1 = letter1.upper()  #将用户输入的字母自动转化为大写
#
# if letter1 in ['T','S']:
# 	letter2 = input('请输入第二个字母：')
# 	print(weeklist[letter1][letter2])
# else:
# 	print(weeklist[letter1])


#方法3：先判断第一个字母，在判断第二个  if（if-else：）-elif-else：
letter = input("please input:")
if letter == 'S':
	print('please input second letter:')
	letter = input("please input:")
	if letter == 'a':
		print('Saturday')
	elif letter == 'u':
		print('Sunday')
	else:
		print('data error')

elif letter == 'F':
	print('Friday')

elif letter == 'M':
	print('Monday')

elif letter == 'T':
	print('please input second letter')
	letter = input("please input:")

	if letter == 'u':
		print('Tuesday')
	elif letter == 'h':
		print('Thursday')
	else:
		print('data error')

elif letter == 'W':
	print('Wednesday')
else:
	print('data error')


