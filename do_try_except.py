#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
2、所有错误类型，Exception 是其他大部分异常的统筹
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
3、使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错
了，这时，只要main()捕获到了，就可以处理：
4、只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
尽量使用Python内置的错误类型。
'''
# try:
# 	print ('try...')
# 	r = 10/0  #如果代码出错，则从出错的地方 跳过，直接到except模块，如果不出错，则继续执行try 后直接跳到finally模块
# 	print ('result:',r)
# except ZeroDivisionError as e:  #except主要是用于定于可能出现的错误类型并输出
# 	print ('except',e)
# finally:
# 	print ('finally...') #不过是否出错都会执行
#
# print ('END')
#
# #若可能发生多种错误，可以使用多个except来捕获
# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
# 	print ('no error') #如果没有错误。则执行else模块
# finally:
#     print('finally...')
# print('END')
#
# #捕捉跨级调用错误
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
#

# #分错报错信息：
# import logging #日志模块，可以实现出现问题记录日志但是不终止程序
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()
# print ('END')


# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0') # 这个foo（）函数会raise错误，但是被try-except截获，因此会根据它的机制来处理，但是这个遇到了raise 因此会将错误抛出
#     except ValueError as e:
#         print('ValueError!')
#         raise #抛出错误
# bar()

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)  #这个raise 总是向上抛出错误，由最外层接收处理
    return 10 / n
foo('0')


#练习题
from functools import reduce

def str2num(s):
	try:
    	 return int(s)
	except ValueError as e:
		print (e)
		n = float(s)
	return n


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns) #lambda acc, x: acc  这个是reduce的函数参数，后面的ns是取值范围

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r1 = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r1)

main()
