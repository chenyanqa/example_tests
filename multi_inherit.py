#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、是A中没有就去B中找；
而在B中找就是找B以及B的父类。
这就是个树的前序遍历，根节点然后从左往右的遍历子树
所以顺序是：A、BED、CDF

2、多重继承
要让一个类 同时具备多种功能，可以让他分别继承已经具备该功能的父类即可-》这种实现的过程就叫Mixin

3、Mixin的目的就是给一个类 增加了多个功能，在设计类的时候，优先考虑通过多重继承来组合多个Mixin的功能，而不是通过设计多层次的复杂继承关系

4、解析：
'''
import inspect

class G(object):
    pass

class D(object):
    def __init__(self):
        print("D")


class E(object):
    def __init__(self):
        print("E")


class F(object):
    def __init__(self):
        print("F")


class C(D, F):
    def __init__(self):
        print("C")


class B(E, G):
    def __init__(self):
        print("B")


class A(B, C):
    def __init__(self):
        print("A")


if __name__ == '__main__':
    print(inspect.getmro(A))
#输出(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.G'>, <class '__main__.C'>,
# <class '__main__.D'>, <class '__main__.F'>, <class 'object'>)


# #案例二：Python 自带了TCPServer 和UDPServer 这两类网络服务，如果要同时服务多个用户 就必须使用多进程，多线程模式，这两种
# #模式由ForkingMixIn 和ThreadingMixIn提供，通过组合，就可以设计出期望的效果，如：
#
# class MyTCPServer(TCPServer,ForkingMixIn):  #编写一个多线程模式的TCP服务
#     pass
#
# class MyUDPServer(UDPServer,ThreadingMixIn): #编写一个多线程模式的UDP服务
#     pass
#

#案例三：动物（哺乳动物、鸟类），（能飞的，能跑的）

class Animal(object):
    pass

class Mammal(Animal): #哺乳类
    pass

class Bird(Animal):  #鸟类
    pass

class Dog(Mammal): #狗类
    pass

class Bat(Mammal): #蝙蝠类
    pass

class Parrot(Bird): #鹦鹉类
    pass

class Ostrich(Bird): #鸵鸟类
    pass

#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass

#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass