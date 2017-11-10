#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#使用lambda来创建匿名函数。
'''
1、lambda 主要用来创建匿名函数，def 用来创建带名称的函数
2、lambda 是一个表达式（可以快速创建单行最小函数），而 def 是一个函数语句
3、lambda 可以直接把函数赋值给一个变量，用变量名来表示函数名，并且调用
4、lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值，lambda 函数不能包含命令，包含的表达式不能超过一个
5、lambda的一般形式是关键字lambda后面跟一个或多个参数，紧跟一个冒号，以后是一个表达式（相当于函数体）。lambda是一个表达式而不是一个语句。
它能够出现在Python语法不允许def出现的地方。作为表达式，lambda返回一个值（即一个新的函数）。lambda用来编写简单的函数，
而def用来处理更强大的任务。

6、实例：
def f ( x ,y):
    return x * y
f ( 2,3 )  #输出 6

g = lambda x ,y: x * y
g ( 2,3 )  #输出 6

'''

# lambda x:print(x)  #返回为none，因为它只是创建了一个函数对象, 但是没有被调用
# print(lambda x:print(x))  #返回<function <lambda> at 0x100761e18> ，print（）不适应于lambda

# g = lambda x:print(x+2)  #lambda 的正常使用：需要先将lambda 表达式赋值给一个变量，然后通过这个变量来调用
# print(g(3))


MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y    #这里 （x > y） 如果为真 则返回1，如果为假，则返回0
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x   #lambda 可以有多个 参数，但是只能有一个表达式

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar one is %d' % MAXIMUM(a, b))
    print('The lower one is %d' % MINIMUM(a, b))
