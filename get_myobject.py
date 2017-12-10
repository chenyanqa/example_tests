#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、获取对象信息的方法 dir()- 主要针对类对象，isinstance() --可针对所以对象，例如类，字符串，整型，列表，字典等
type（）--一般仅仅针对普通对象，例如字符串，列表等
2、hasattr（obj，'attr'） 等方法是python内置函数，并非对象的函数
3、hasattr（）、getattr（）等针对私有变量和方法并不适用
4、__init__（）方法中，如果定义了 参数，则在实例化对象的时候 就必须传入参数，否则 不用传
5、def __init__(self,x): #这里的x 表示初始化实例的时候 需要传入的参数x
		self.x = x  #这里的self.x 表示类的属性x
6、print(setattr(obj,'y',19))  #给属性赋值，若属性不存在，则生产一个并赋值，若存在则改变其原值
7、print(getattr(obj,'z',404)) #获取属性‘z’的值，如果z不存在，则返回默认值404
8、print(getattr(obj,'power')) #<bound method Myobject.power of <__main__.Myobject object at 0x00000128BBD965C0>>
'''
#案例1：
class Myobject(object):
	# 如果类的构造函数这样定义的话，那么创建对象时，就必须传入参数x的值，因为实例变量self.x 的值，是拿实参来赋值的
	# def __init__(self,x): #这里的x 表示初始化实例的时候 需要传入的参数x
	# 	self.x = x  #这里的self.x 表示类的属性x

	def __init__(self): #如果这样定义构造函数的话，那么创建对象的时候，无需传入实例变量的值，因为这里直接给其赋了一个固定值
		self.x = 9

	def power(self):
		return self.x*self.x

# obj = Myobject(9)
obj = Myobject()
print(dir(obj))  #获取对象的所有属性和方法

#获取对象的属性 （以下函数对私有变量和属性无效）
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
print(setattr(obj,'y',19))  #给属性赋值，若属性不存在，则生产一个并赋值，若存在则改变其原值
print(hasattr(obj,'y'))  #判断对象是否有属性’y‘ ，返回值会布尔型
print(getattr(obj,'y')) #获取对象的属性‘y’
print(obj.y) #通过对象调用其属性
print(getattr(obj,'z',404)) #获取属性‘z’的值，如果z不存在，则返回默认值404

print(len('abc'))
print('abc'.__len__()) #字符串对象'abc'包含__len__()方法，其实调用内置函数len（'s'）方法就是在字符串对象的特殊方法

#获取对象的方法
print(hasattr(obj,'power'))
print(getattr(obj,'power')) #<bound method Myobject.power of <__main__.Myobject object at 0x00000128BBD965C0>>

fn = getattr(obj,'power')
print(fn) #<bound method Myobject.power of <__main__.Myobject object at 0x00000259795F65F8>>
print(fn())

sum = obj.x +obj.y
print(sum)


#案例二：
def read_image(fp):
	if hasattr(fp,'read'):  #判断fp对象 是否有read方法
		return read_Data(fp)
	else:
		return None