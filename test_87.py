#!/usr/bin/env python
# -*- coding:utf-8 -*-
#题目：回答结果（结构体变量传递）。
'''
class A:
 x = 0
 def __init__(self):
 self.y = 0
x就是类变量，y就是实例变量。
'''

if __name__ == '__main__':
    class student:
        x = 0   #x，c 都是类变量
        c = 0

    def f(stu):
        stu.x = 20  #stu.x 为局部变量
        stu.c = 'c'

    a= student() #a为student的一个实例变量
    a.x = 3   #相当于两个全局变量
    a.c = 'a'

    f(a)
    print(a.x,a.c)  #如果调用的函数 有局部变量 则优先使用局部变量