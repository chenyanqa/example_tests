#!/usr/bin/env python
# -*- coding:utf-8 -*-

#实例属性和类属性

# class Student(object):
# 	name = 'Student' #定义类属性
# 	score = 90
#
# 	def __init__(self,name):
# 		self.name = name  #定义实例属性
#
# s = Student('Bob')  #创建实例s
# print (s.name)  #输出实例属性
# print (s.score) #会先去寻找实例属性，如果没有找到的话，再去遍历类属性并输出，因为实例可以访问类属性
# print (Student.name) #使用类名调用类属性
# print (Student.score)
# s.score = 100
# print (s.score)
# print (Student.score)
# del s.score   #解除实例属性的绑定
# print (s.score)


#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
	count = 0
	def __init__(self,name):
		self.name = name
		#count = count+1
		Student.count += 1  #如果在类方法中要访问类变量，需要使用类+属性的方式读取

a = Student('Bob')
b= Student('sana')
print(Student.count) #类属性的读取
