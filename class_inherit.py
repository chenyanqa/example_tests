#!/usr/bin/env python
# -*- coding:utf-8 -*-

#类的继承和多态
'''
继承：
1、子类可以继承父类的所有共有的方法和属性，并且对父类中的方法进行改写，同时也可以新增
2、子类的实例 可以被当做父类的实例，但是反过来不行。

多态：（一个方法、对象呈现多种形态，例如本例中的 run（）方法）
1、例如需要增加一个子类时，任何依赖父类的方法或者函数可以不加任何修改，可以被新增子类正常使用
2、多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……
都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或
者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
3、对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作
用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我
们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

鸭子类型：
它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方
法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现
了read()方法的对象。
'''
class Animal(object): #定义父类
	def run(self):  #父类中含有run()方法
		print ('Animal is running...')

class Dog(Animal):  #Dog类继承父类Animal
	def run(self):  #改写继承和父类的方法
		print('Dog is running... ')

class Cat(Animal):
	def run(self):
		print ('Cat id running...')

class Tortoise(Animal):
	def run(self):
		print ('Tortoise is running slowly...')

class Timer(object): #Timer类跟Animal类无任何关系，只是长得有点像而已 （鸭子类型）
	def run(self):
		print ('Start...')

class Timer1(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print ('%s的分数为%s'%(self.name,self.score))


def run_twice(cc):  #在类的外部定义了一个函数，接收类似animal等类的实例，然后进行对应操作
	cc.run()  #这个实例参数调用各类的类方法，因此只要某个类实现了对应的方法，且正常结果一致，也可以调用该函数
	cc.run()

a = Animal()
b = Dog()
c = Cat()
d = Tortoise()
e = Timer()
f = Timer1('chen',90)

print ('a is Animal?',isinstance(a,Animal))  #isinstance（）判断某个实例是否是某个数据类型
print ('a is Dog?',isinstance(a,Dog))
print ('a is Cat?',isinstance(a,Cat))

print ('b is Animal?',isinstance(b,Animal))
print ('b is Dog?',isinstance(b,Dog))
print ('b is Cat?',isinstance(b,Cat))

print ('e is Animal?',isinstance(e,Animal))
print ('e is Animal?',isinstance(e,Dog))
print ('e is Animal?',isinstance(e,Cat))

#多态：就是某个依赖父类的方法，在传入其子类后 都可以当成父类的方式去运行，不过此时在运行的过程中，会优先根据当前传入
#实际子类及子类改写后的方法 去实际变更
run_twice(c)
run_twice(d)
run_twice(e)
f.print_score()

'''
#静态语言
public void getName(Person p){  #方法定义时传入的参数必须指定类型，必须是鸭子才可以调用
	
} 
#动态语言
def get_name(p)  #方法定义时 传入的参数 可以是任意类型的，因此只要长得像（看起来像鸭子-表示整体外观结构像，走起路来也像
-表示里面的方法，操作像，比如都实现了必要的方法），就认为是鸭子，就可以调用鸭子才能使用的特权
'''

print(type(e))
print (e)
print(type(f))
print(f)
print(dir(f))