#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、元类：即用来创建所有类的类，相当于类工厂，所有的类都是元类的实例，而tpye是python的内置元类，当然用户也可以自定义元类
，但是需要默认继承type类
2、创建类可以通过在python中最终都是调用type（）方法，Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
3、__metaclass__属性 里面放置一些可以用来创建类的东西，如果你写一个类的时候 为其添加了该属性，则python会优先按照__metaclass__
中的规则和方法来创建类。metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
4、也就是说metaclass的实例化结果是类，而class实例化的结果是instance
5、一般情况下, 如果你要用类来实现metaclass的话，该类需要继承于type，而且通常会重写type的__new__方法来控制创建过程。
6、在metaclass里面定义的方法会成为类的方法，可以直接通过类名来调用
7、对于python而言，metaclass使程序员可以干涉class的创建过程，并可以在任何
时候修改这样的class(包括修改metaclass)，由于class的意义是为instance集合
持有“方法”，所以修改了一个class就等于修改了所有这些instance的行为，这是
很好的service。
8、
'''
#定义元类，给类对象增加一个add（）方法
class ListMetaclass(type): #metaclass的类 总是以Metaclass结尾，且默认继承type内置元类
	def __new__(cls, name, bases,attrs): #__new__用于创建类并返回类，cls指类对象（元类的实例）
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)


#使用元类
class MyList(list,metaclass=ListMetaclass): #python解释器在创建MyList类时，优先通过ListMetaclass自定义元类中规则来创建
	pass

#直接通过类名调用会报错，因为原来中是lambda函数是需要创建该类的实例来调用的
#print (MyList.add(1))  #TypeError: <lambda>() missing 1 required positional argument: 'value'
L =MyList() #由于MyList
L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)
# L1  = list()
# L1.add(1)   #AttributeError: 'list' object has no attribute 'add' 会报错，因为普通list 没有添加add（）方法



