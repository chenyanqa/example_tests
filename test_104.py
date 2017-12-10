#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、class 是用来定义类的关键字，类名首字母须大写，括号里面是表示当前自定义的类从哪个类继承下来的，
2、如果没有合适的继承类，就默认写object类，因为object类是所有类最终都会集成的类
3、由于类起到模板的作用，可以通过__init__()方法在创建实例的时候，把一些必要的属性强制绑定上去。
4、__init__(self,属性1，属性2) 该方法第一个参数默认为实例本身，因此添加的属性也是默认绑定到实例上的，有了这个模板以后
在真正创建实例的时候，属性1和属性2 就是2个必传参数了。
5、类中的方法和普通函数大致的定义和用法一致，只有一点不同，类中的方法定义时 ，第一个参数默认为实例变量self，但是调用时可以不用传
6、类之所以能起到数据封装的作用就是因为 类的内部含有属性和对属性的操作以及一些其他逻辑，外部看来，我只要知道这个类怎么创建一个实例
然后类里面提供了那些方法，可以用来完成什么功能即可，具体类里面这些逻辑、功能、数据怎么流转和实现的，我不用知道 也不关心。
属性
7、除了在类定义的属性外，实例也可以在类外自定绑定其他属性
'''
class Students(object): #类相当于是一个适用于某类事物的统一模板
	def __init__(self,name,score): #类的构造函数，用于在创建实例的时候强制绑定一些属性在实例上
		self.name = name
		self.score = score

	def print_score(self):#类的方法，绑定在实例上，用于定义对属性的操作
		print('%s:%s' % (self.name,self.score))

	def get_score(self):
		if self.score < 60:
			print ('不及格')
		elif self.score in [60,90]:
			print('良好')
		else:
			print('优秀')

#bart = Students() #TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
bart = Students('bart',80) #必须按照类的构造函数的要求来创建实例
bart.age = 20  #实例也可以在类外面自行绑定其他属性
print('bart age：%s'%bart.age)
lisa = Students('lisa',70)

bart.print_score() #调用类方法
bart.get_score()

print (bart)  #<__main__.Students object at 0x00000249947165C0> 表示bart是类Students类的一个对象，以及在内存中的地址
print (Students) #<class '__main__.Students'>
