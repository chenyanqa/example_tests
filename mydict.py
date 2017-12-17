#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、单元测试：针对一个模块、函数、类来进行正确性检验的测试工作
2、这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证
该模块行为仍然是正确的。
3、对于super(B, self).__init__()是这样理解的：super(B, self)首先找到B的父类（就是类A），然后把类B的对象self转换为类A的对象
，然后“被转换”的类A对象调用自己的__init__函数

'''

class Dict(dict):
	def __init__(self,**kv):
		super(Dict, self).__init__(**kv) #调用父类的构造方法，super(Dict, self)先去寻找Dict的父类，然后将当前类实例self转换为父类实例

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError('Dict object has no attribute %s'%key)
	def __setattr__(self, key, value):
		self[key] = value

		
