#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#定制类：在定义类的时候 可以通过修改python内置的一些特殊函数来更好的实现定义的类

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __str__(self):  #定制__str__方法
        return '(Person:%s,%s)' %(self.name,self.gender)



    __repr__ = __str__


    def __cmp__(self, s): #定制__cmp__方法
        if self.name <s.name:
            return -1
        elif self.name >s.name:
            return 1
        else:
            return 0




