#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、class 中的属性如果不希望被外部访问或者改变，可以将其设置为私有的，加上前双下划线即可,例如__name （private）
2、这样可以进行访问限制，使代码更加健壮，同时可以提供get_name() 等方法供外界调用 或者内部属性
3、如果外部需要修改属性值，那么可以在类方法中增加类似 set_name() 的方法 供外界调用，同时可以通过方式对用户的设置值进行校验，
避免传入无效参数
4、在python中类似__xxx__ 双下划线开头、结尾的变量属于特殊变量（一般表示系统内置的一些属性），外部是可以直接访问的
5、有时候可以看到单下划线开头的实例变量，例如_name 这种变量外部可以访问，但是一般看到这样的变量 ，默认的意思就是，“虽然
我可以被访问，但是，请把我视为私有变量，不要随意访问”。
6、双下划线开头的变量 不能直接被外部访问，但是由于一般解释器会默认把它加以转换，例如__name,会被转为_Student__name,所有
可以通过访问_Student__name 实现对私有变量的访问，但是一般不建议这么做，因为不同的解释器可能转换出来的名称不一致，兼容性差
'''
# class Student(object):
#
# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score
#
# 	def print_score(self):
# 		print('%s:%s' %(self.__name,self.__score))
#
# 	def get_name(self):
# 		return self.__name
#
# 	def get_score(self):
# 		return self.__score
#
# 	def set_score(self,score):
# 		#if score in [0,100]:  #[0.100] 有的时候不一定可以表示区间，有时候可能就表示一个列表，仅有0,100两个元素
# 		if 0<= score <=100:
# 			self.__score = score
# 		else:
# 			raise ValueError('bad score')
#
# bart = Student('bart',90)
# lisa = Student('lisa',60)
# bart.print_score()
# #print(bart.get_score()+lisa.get_score())
# print(bart.get_name(),lisa.get_name())
# print(bart.get_score())
# #bart.set_score(800)
# bart.set_score(90)

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self,gender):
		if gender in ['male','female']:
			self.__gender = gender
		else:
			raise ValueError('输入错误！')

bart = Student('bart','male')
print(bart.get_gender())
bart.set_gender('female')
print(bart.get_gender())

