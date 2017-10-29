#!/usr/bin/env python
# -*- coding:utf-8 -*-

#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# #方法1：
# score = int(input('请输入学生成绩：'))
# if score >= 90:
# 	print('A')
# elif 60 <= score <=89 :
# 	print('B')
# else:
# 	print('C')


#方法2：
def grade(x):
	if x in range(60):
		print('C')
	elif x in range(60,90):
		print('B')
	else:
		print('A')
score = int(input('请输入学生成绩：'))

grade(score)
