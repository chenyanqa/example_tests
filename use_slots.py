#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1、由于python语音的动态性，决定了变量或者实例的 可以绑定任意不同类似的属性和方法而不受数据类型的限制
2、给实例绑定属性，可以直接用实例.属性的方法，例如s.name = 'Bob'
3、除了绑定任意属性外，还可以任意绑定方法，例如有新增方法set_age， 给类绑定方法：Student.set_age = set_age ，此时该类下的所有实例均可调用该方法
4、给某实例绑定方法，s.set_age = types.MethodType(set_age,s) ，此时进该实例可以调用，其他实例不行
5、可以使用类的内置变量 __slots__来限制属性或者方法的任意绑定，例如__slots__= ('name','age','set_age')，元组的形势
6、__slots__ 变量仅对当前类的实例生效，对其子类的限制不生效
7、try-except 异常捕捉：将可能出错的代码放在try模块，在except 模块下 定义需要捕捉那些基本的异常或者用什么方法捕捉，并输出异常
'''
#from types import MethodType
import types
class Student(object):
	# __slots__作为类内置的一个特殊变量，可以用来限制类实例能添加的属性，是一个tuple的形式（因为tuple是不可变的）
	# 该变量只能作用于当前类的实例，对其子类的实例 没有限制作用
	__slots__= ('name','age','set_age')

class GraduateStudent(Student):
	pass

def set_age(self,age):
	self.age = age

s = Student()
s.name = 'Bob'  #实例绑定name变量
s.age = 20
print (s.age)

#给类或者实例绑定方法
#Student.set_age = set_age #给类绑定方法，后续该类的所有实例 都可以调用set_age（）方法
s.set_age = types.MethodType(set_age,s) #由于Student使用了__slots__ 变量，因此无法把set_age这个属性加上。
s.set_age(25)
print (s.age)

#try-except ：except 模块主要定义捕捉那些异常 或者捕获异常的方式，例如Exception、traceback等
try:
	s.score = 99 #将可能出错的代码放在try下
except AttributeError as e:   #except 模块用来处理异常：打印异常，且不中断程序，此处知道仅仅关注AttributeError即可
	print ('AttributeError:',e)
# except Exception as e: #如果之前不知道可能会出现什么错误，可以默认捕获所有的异常Exception
# 	print (e)


g = GraduateStudent() #创建子类实例
g.score = 99  #给实例绑定属性score  可以绑定成功，因为父类的__slots__变量限制不了子类
print (g.score)

#print(dir(s))