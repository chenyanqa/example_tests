#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、为了类属性的安全，一般会限制外部直接读取类属性及赋值，所以可以将属性设置为私有变量，然后在类里面定义一个获取属性get_attr()
和设置属性 set_attr() 的方法、同时可以方便检查参数，然后提供外部调用，只不过步骤繁琐了些
2、为了简化操作，可以使用python 内置的 @property 装饰器 负责把一个方法变成属性调用
3、


'''

class Student(object):

	@property  #可以把getter()方法变成属性
	def score(self):
		return self._score #当成私有变量

	@score.setter  #可以把setter（）方法变成属性赋值
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value <0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student()
s.score =60   #实际转换为s.set_score(60)
print('s.score =',s.score) #实际转换为 s.get_score()
s.score = 9999