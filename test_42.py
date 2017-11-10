#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
题目：学习使用auto定义变量的用法。
程序分析：没有auto关键字，使用变量作用域来举例吧。

python能够改变变量作用域的代码段是def、class、lamda.
if/elif/else、try/except/finally、for/while 并不能涉及变量作用域的更改，也就是说他们的代码块中的变量，在外部也是可以访问的
变量搜索路径是：本地变量->全局变量
 '''
#num = 10

def autofunc():
    num1 = num+1
    print('internal block num = %d' % num1)
    num1 += 1
   


num = 10  #当前代码块中 变量一律用num=10，但是调用函数时，由于没有传任何变量，因此使用函数的局部变量 ，值为1
for i in range(3):
    print('The num = %d' % num)
    num += 1

    #autofunc(num1)    这句语法会报错，因为num1为局部变量，只能在autofunc（）内部实现函数逻辑的时候调用
    autofunc()
    '''
    如果当前autofunc（）定义的时候 是一个形参的函数，则此时调用的时候 可以把实参带过去，该实参会在函数中起到作用 
    '''




