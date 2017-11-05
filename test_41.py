#!/usr/bin/env python
# -*- coding:utf-8 -*-

#模仿静态变量的用法

def varfunc():
	var = 1  # 定义一个局部变量，并赋予默认值并在初始化的时候调用，后续将不再改变同一变量的此值
	print('var = %d' % var)
	var1 = var + 1  #此时var1变量的初值为2
	print('var = %d' % var1)


if __name__ == '__main__':  # 表示仅当前脚本执行以下代码，被引入其他模块时 不执行以下代码
	for i in range(3):  # i=0 时，执行varfun（）函数，输出var=0,
		varfunc()


# #类的属性，作为类的一个属性
# class Static:
#     StaticVar = 5  #定义一个类的静态变量
#     def varfunc(self):
# 		# 定义一个实例变量, self.StaticVar = self.StaticVar+1  ,self.StaticVar的初值取得是静态变量
#         self.StaticVar += 1
#         print(self.StaticVar)
#
# print(Static.StaticVar)   #调用静态变量
# a = Static()   #实例化一个类的对象
# for i in range(3):
#     a.varfunc()


# class test:
#     l=[]  #定义一个静态变量
#     def init(self):
#         self.l=[1,2,7]   #定义一个实例变量（python中 遇到赋值语句会默认新生成一个变量）
# a1=test()
# a1.init()
# print(a1.l)
# print(test.l)  #他指向的是 静态变量


# class test:
#     l=[]   #定义一个静态变量
#     def init(self):
#         self.l.append(1)  #这里相当于使用test.l.append()方法修改静态变量
#         self.l.append(2)
#         self.l.append(7)
#
# a1=test()  #定义类的实例变量a
# a1.init()
# print(a1.l)  #a1.l 在没有实例变量时， 相当于是self.l(在类内部使用) 及test.l
# print(test.l)


# #静态变量、局部变量、实例变量使用
# class A(object):
# 	va = 10  #类变量（静态变量）
#
# 	def foo(self):
#
# 		print (A.va)  #读取静态变量
# 		print (self.va)  #读取静态变量
#
# 		self.va = 40  #定义一个实例变量
# 		print (A.va)  #静态变量不受影响，仍然为10
# 		print (self.va)  #此时self.va 为实例变量 40
#
# 		va = 20    #定义一个局部变量
# 		print (va)
#
# 		A.va = 15  #将静态变量重新赋值为 15
# 		print (A.va)
# 		print (self.va)
#
# obj1 = A()
# obj2 = A()
# obj1.foo()
# print()
# print(A.va)  #obj1.foo()执行后，类变量的值已经变为15了。
# print()
# print(obj1.va)
# print()
# print(obj2.va)   #此时obj2 实例由于没有调用foo（）方法，因此obj2.va相当于实在读取类变量